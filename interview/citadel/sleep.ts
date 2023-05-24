const testSleep = async (type: "parallel" | "sequential") => {
  const start = performance.now();
  const fn = type === "parallel" ? sleepParallel : sleepSequential;
  await fn(1_000, 2_000, 3_000);
  console.log(`<${type}> Slept for ${performance.now() - start}`);
};

const main = async () => {
  await testSleep("parallel"); // 3 seconds
  await testSleep("sequential"); // 6 seconds
};

const sleep = (time: number) => {
  return new Promise((resolve) => setTimeout(resolve, time));
};

const sleepParallel = (...times: number[]) => {
  return Promise.all(times.map(sleep));
};

const sleepSequential = async (...times: number[]) => {
  for (const time of times) {
    await sleep(time);
  }
};

main();

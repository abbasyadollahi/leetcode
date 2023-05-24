import { useEffect, useRef, useState } from "react";

const URL =
    "https://wgg522pwivhvi5gqsn675gth3q0otdja.lambda-url.us-east-1.on.aws/717561";

const Typewriter = (props) => {
    const [letters, setLetters] = useState("");
    const lettersRef = useRef("");

    useEffect(() => {
        const interval = setInterval(() => {
            if (lettersRef.current.length < props.text.length) {
                setLetters((previous) => {
                    lettersRef.current = props.text.slice(0, previous.length + 1);
                    return lettersRef.current;
                });
            } else {
                clearInterval(interval);
            }
        }, props.delay);

        return () => {
            clearInterval(interval);
        };
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
        <ul>
            {[...letters].map((letter, index) => {
                return <li key={index}>{letter}</li>;
            })}
        </ul>
    );
};

const App = () => {
    const [flag, setFlag] = useState("");

    useEffect(() => {
        fetch(URL)
            .then((response) => {
                return response.text();
            })
            .then((text) => {
                setFlag(text);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    return (
        <div className="App">
            <h1>Hello Ramp!</h1>
            {flag ? <Typewriter text={flag} delay={500} /> : <>Loading...</>}
        </div>
    );
};

export default App;

// Script used to find URL in step 2
// [...document.querySelectorAll("section[id^='11'] > main[id$='22'] > article[id*='33'] > p.flag")]
//     .map((p) => p.getAttribute("value"))
//     .join();

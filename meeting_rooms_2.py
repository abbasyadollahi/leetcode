class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        if not intervals:
            return 0

        timeline = []
        for i in intervals:
            timeline.append(('s', i.start))
            timeline.append(('e', i.end))

        timeline = sorted(timeline, key=lambda x: (x[1], x[0]))

        room = 0
        max_room = 0
        for k, v in timeline:
            if k == 'start':
                room += 1
            else:
                room -= 1
            if room > max_room:
                max_room = room

        return max_room

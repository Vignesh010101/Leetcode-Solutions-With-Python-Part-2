class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        total_creators = len(creators)
        max_total_views = None
        most_viewed_creators = {}
        creator_index = {}

        for i in range(total_creators):
            creator = creators[i]
            if creator not in creator_index:
                creator_index[creator] = {
                    "total_views": 0,
                    "most_viewed_id": None,
                    "most_views": None,
                }

            creator_index[creator]["total_views"] += views[i]
            if len(most_viewed_creators) == 0:
                most_viewed_creators = {creator: True}
                max_total_views = views[i]
            elif creator_index[creator]["total_views"] > max_total_views:
                max_total_views = creator_index[creator]["total_views"]
                most_viewed_creators = {creator: True}
            elif creator_index[creator]["total_views"] == max_total_views and creator not in most_viewed_creators:
                most_viewed_creators[creator] = True

            if creator_index[creator]["most_viewed_id"] is None:
                creator_index[creator]["most_viewed_id"] = ids[i]
                creator_index[creator]["most_views"] = views[i]
            elif views[i] > creator_index[creator]["most_views"]:
                creator_index[creator]["most_viewed_id"] = ids[i]
                creator_index[creator]["most_views"] = views[i]
            elif views[i] == creator_index[creator]["most_views"] and ids[i] < creator_index[creator]["most_viewed_id"]:
                creator_index[creator]["most_viewed_id"] = ids[i]
                creator_index[creator]["most_views"] = views[i]

        result = [
            [creator, creator_index[creator]["most_viewed_id"]]
            for creator in most_viewed_creators.keys()
        ]
        return result
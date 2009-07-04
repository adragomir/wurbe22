from util import json

stri = """
[
    {
        "updated": new Date(2009,3,5,16,34,53), 
        "via": {
            "url": "http:\/\/friendfeed.com\/share\/bookmarklet", 
            "name": "Bookmarklet"
        }, 
        "service": {
            "profileUrl": "http:\/\/friendfeed.com\/davew", 
            "iconUrl": "http:\/\/friendfeed.com\/static\/images\/icons\/internal.png?v=e471e9afdf04ae568dcbddb5584fc6c0", 
            "id": "internal", 
            "name": "FriendFeed", 
            "entryType": "link"
        }, 
        "title": "Nature Made Vitamin C, 1000 mg, Premium Tablets, Value Size, 300 premium tablets", 
        "media": [
            {
                "enclosures": null, 
                "title": null, 
                "content": [
                    {
                        "url": "http:\/\/ecx.images-amazon.com\/images\/I\/41AJF9K9QNL._SL500_AA280_.jpg", 
                        "width": 280, 
                        "type": "image\/jpeg", 
                        "height": 280
                    }
                ], 
                "player": null, 
                "link": "http:\/\/www.amazon.com\/Nature-Made-Vitamin-Premium-Tablets\/dp\/B00008I8NJ\/ref=sr_1_1?ie=UTF8&s=hpc&qid=1238948946&sr=1-1", 
                "thumbnails": [
                    {
                        "url": "http:\/\/i.friendfeed.com\/379c11358a5914d8995c7971fb8f1f34aa7c6bf9", 
                        "width": 175, 
                        "height": 175
                    }
                ]
            }
        ], 
        "comments": [
            {
                "date": new Date(2009,3,5,16,36,49), 
                "body": "Recommended by internet blowhards. ;)", 
                "id": "2de42bf6-1841-4259-96fc-81c61b51a754", 
                "user": {
                    "profileUrl": "http:\/\/friendfeed.com\/jeber", 
                    "nickname": "jeber", 
                    "id": "ab9c7c30-e89e-11dc-8447-003048343a40", 
                    "name": "Jack Carlson"
                }
            }
        ], 
        "link": "http:\/\/www.amazon.com\/Nature-Made-Vitamin-Premium-Tablets\/dp\/B00008I8NJ\/ref=sr_1_1?ie=UTF8&s=hpc&qid=1238948946&sr=1-1", 
        "likes": [], 
        "anonymous": false, 
        "published": new Date(2009,3,5,16,34,53), 
        "hidden": false, 
        "id": "1ca72391-dcec-49fd-898f-deea499b7367", 
        "user": {
            "profileUrl": "http:\/\/friendfeed.com\/davew", 
            "nickname": "davew", 
            "id": "8be56d9f-6650-4aee-8e15-e7791dfe7e66", 
            "name": "Dave Winer"
        }
    }
]
"""

obj = json.loads(stri)

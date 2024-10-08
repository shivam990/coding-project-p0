# Harbor Take Home Project

Welcome to the Harbor take home project. We hope this is a good opportunity for you to showcase your skills.

## The Challenge

Build us a REST API for calendly. Remember to support

- Setting own availability
- Showing own availability
- Finding overlap in schedule between 2 users

It is up to you what else to support.

## Expectations

We care about

- Have you thought through what a good MVP looks like? Does your API support that?
- What trade-offs are you making in your design?
- Working code - we should be able to pull and hit the code locally. Bonus points if deployed somewhere.
- Any good engineer will make hacks when necessary - what are your hacks and why?

We don't care about

- Authentication
- UI
- Perfection - good and working quickly is better

It is up to you how much time you want to spend on this project. There are likely diminishing returns as the time spent goes up.

## Submission

Please fork this repository and reach out to Prakash when finished.

## Next Steps

After submission, we will conduct a 30 to 60 minute code review in person. We will ask you about your thinking and design choices.

## Assumptions
1. Using In-memory Cache to store the data, i.e.. focusing on MVP & business logic.


## Deployment Details

Code is deployed at Railway.
Host Url: https://coding-project-p0-production.up.railway.app/

Use below endpoints to hit the api's:-

1. Save/Update Availability
POST - "/availability/{user_id}"
This API will save & update the list of availabilities provided for a user. Also it is smart enough to detect the adjacent/overlapping intervals, & provides the final merged  availability.

Sample URL: https://coding-project-p0-production.up.railway.app/availability/{user_2}

Sample request json:-
```
{
    "availabilities": [
        {"start_time": "2024-09-15T09:00:00", "end_time": "2024-09-15T11:00:00"},
        {"start_time": "2024-09-15T10:30:00", "end_time": "2024-09-15T12:00:00"},  // This will be merged
        {"start_time": "2024-09-15T14:00:00", "end_time": "2024-09-15T16:00:00"},
        {"start_time": "2024-09-15T14:00:00", "end_time": "2024-09-15T16:00:00"}
    ]
}
```

Sample response json:-
```
{
    "availability": [
        {
            "start_time": "2024-09-15T09:00:00",
            "end_time": "2024-09-15T12:00:00"
        },
        {
            "start_time": "2024-09-15T14:00:00",
            "end_time": "2024-09-15T16:00:00"
        }
    ]
}
```

2. Get Availability - GET
GET - "/availability/{user_id}"
This API would provide the list of availabilities of a particular user.

Sample Url: https://coding-project-p0-production.up.railway.app/availability/{user_2}

Sample Response:-

```
{
    "availability": [
        {
            "start_time": "2024-09-15T09:00:00",
            "end_time": "2024-09-15T12:00:00"
        },
        {
            "start_time": "2024-09-15T14:00:00",
            "end_time": "2024-09-15T16:00:00"
        }
    ]
}
```

3. Find Overlap between two users
GET - "/overlap"
This API provides the oevrlapping of intervals between two users ex- user_1 & user_2

Sample Url: https://coding-project-p0-production.up.railway.app/overlap?user_id_1={user_1}&user_id_2={user_2}

Sample Response:-
```
{
    "overlap": [
        {
            "start_time": "2024-09-15T09:00:00",
            "end_time": "2024-09-15T11:00:00"
        }
    ]
}
```

## Steps to run code in local

1. Clone the repository
git clone git@github.com:shivam990/coding-project-p0.git
cd coding-project-p0

2. Install dependencies:-
pip3 install -r requirements.txt

3. Run the application
uvicorn main:app --reload




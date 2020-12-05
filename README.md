# AoC-badges
Github Action to update the [badges](https://github.com/badges/shields) of your Readme to show your current stats for [Advent of Code](https://adventofcode.com/).

Have a look at these examples:

![](https://img.shields.io/badge/day%20📅-5-blue)
![](https://img.shields.io/badge/Stars%20⭐-10-yellow)

## Setup
First of all you have to add the badges to your README. 
Note that if you want to customize the badges you might have to tweak the regeular expressions used to match your badges.
Here are the default ones:

| Badge                                                | Raw Badge                                              |
|------------------------------------------------------|--------------------------------------------------------|
| ![](https://img.shields.io/badge/day%20📅-5-blue)     | `![](https://img.shields.io/badge/day%20📅-5-blue)`     |
| ![](https://img.shields.io/badge/Stars%20⭐-10-yellow) | `![](https://img.shields.io/badge/Stars%20⭐-10-yellow)` |

The default values for the regular expressions can be found in the [`actions.yml`](https://github.com/joblo2213/AoC-badges/blob/master/action.yml)
if you need to tweak them.

Next you have to obtain your session and your user id.  
Go to [Advent of Code leaderboards](https://adventofcode.com/2020/leaderboard/private) and click on `[View]` to visit your private leaderboard.
Then heave a look at the url, the numbers in the end are your user id:

```
https://adventofcode.com/2020/leaderboard/private/view/<youruserId>
```

To get your session secret press F12 while you are logged in on [adventofcode.com](https://adventofcode.com/) to open the developer tools of your browser. 
The open the `Application` Tab on Chromium Browsers or `Storage` on firefox. There you can have a look at your cookies and copy the session id.

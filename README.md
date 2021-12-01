# AoC-badges
Github Action to update the [badges](https://github.com/badges/shields) of your Readme to show your current stats for [Advent of Code](https://adventofcode.com/).

Have a look at these examples:

![](https://img.shields.io/badge/day%20📅-6-blue)
![](https://img.shields.io/badge/stars%20⭐-12-yellow)

## Setup
First of all you have to add the badges to your README.
You can use only some of them or even customize them to fit your needs.  
Note that if you want to customize the badges you might have to tweak the regeular expressions used to match your badges.
Here are the default ones:

| Badge                                                    | Raw Badge                                                 | Description                                            |
|----------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------------|
| ![](https://img.shields.io/badge/day%20📅-6-blue)        | `![](https://img.shields.io/badge/day%20📅-6-blue)`       | Displays the current calendar day                      |
| ![](https://img.shields.io/badge/stars%20⭐-12-yellow)   | `![](https://img.shields.io/badge/stars%20⭐-12-yellow)`  | Displays the total amount of collected stars           |
| ![](https://img.shields.io/badge/days%20completed-6-red) | `![](https://img.shields.io/badge/days%20completed-6-red)` | Displyas on how many days you completed all tasks      |

The default values for the regular expressions can be found in the [`actions.yml`](https://github.com/joblo2213/AoC-badges/blob/master/action.yml)
if you need to tweak them.

The action will search through your readme and updates all badges it finds using the provided (or default) regular expressions.

Next you have to obtain your session and your user id.  
Go to [Advent of Code leaderboards](https://adventofcode.com/2020/leaderboard/private) and click on `[View]` to visit your private leaderboard.
Then heave a look at the url, the numbers in the end are your user id:

```
https://adventofcode.com/2020/leaderboard/private/view/<youruserId>
```

To get your session secret press F12 while you are logged in on [adventofcode.com](https://adventofcode.com/) to open the developer tools of your browser.  
Then open the `Application` Tab on Chromium Browsers or `Storage` on firefox. There you can have a look at your cookies and copy the session id.
You need to add this session id as [encrypted secret](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository) to your repository.

Now you can set up the workflow. The sample workflow beyond will help you.  

If you want to set up badges for multiple years in one repository just add this action multiple times (once for each year using the `year` input).  
Have slightly different badges for each year with a custom regex using the regex inputs.  
The day badge probably doesn't makes sense for multiple years as it only depends on the current date (and therefore only works in December).

## Sample Workflow

```yml
name: Update AoC Badges
on:
  schedule:                                      # run workflow based on schedule
    - cron: '6 5 1-25 12 *'                      # from the 1. December till 25. December every day at 5:06am (avoid load at full hours)
    
  workflow_dispatch:                             # allow to manually start the workflow 
  
# push:                                          # (disabled) run on push, be carefull with this setting 
                                                 # as the workflow should only be triggered at a rate lower than
                                                 # 4 times a hour to keep traffic on aoc site low 
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2                # clones your repo
          
      - uses: joblo2213/aoc-badges-action@v3
        with:
          userid: 00000                          # your user id, see setup on how to obtain
          session: ${{ secrets.AOC_SESSION }}    # secret containing session code, see setup on how to obtain
          
#         Optional inputs:
#         
#         year: 2021                                                                                     # The year for which stats should be retrieved
#         leaderboard: 'https://adventofcode.com/2020/leaderboard/private/view/00000.json'               # The url of the leaderboard from witch the data is fetched. Typically your private leaderboard.
#         file: 'README.md'                                                                              # The file that contains the badges
#         dayRegex: '(?<=https:\/\/img\.shields\.io\/badge\/day%20📅-)[0-9]+(?=-blue)'                   # Regular expression that finds the content of the day badge iun your file.
#         starsRegex: '(?<=https:\/\/img\.shields\.io\/badge\/stars%20⭐-)[0-9]+(?=-yellow)'             # Regular expression that finds the content of the stars badge iun your file.
#         daysCompletedRegex: '(?<=https:\/\/img\.shields\.io\/badge\/days%20completed-)[0-9]+(?=-red)'  # Regular expression that finds the content of the days completed badge iun your file.

      - uses: stefanzweifel/git-auto-commit-action@v4     # Step that pushes these local changes back to your github repo
        with:
          commit_message: Update badges
          file_pattern: README.md
```

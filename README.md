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
The open the `Application` Tab on Chromium Browsers or `Storage` on firefox. There you can have a look at your cookies and copy the session id.

At last make sure you have a [ssh deploy key](https://docs.github.com/en/free-pro-team@latest/developers/overview/managing-deploy-keys#deploy-keys) 
with which you can push to your repo.  
Add the deploy keys private key and your aoc session code as [encrypted secrets](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository) to your repository.  

Now you can set up the workflow. Look at this sample:

## Sample Workflow

```yml
name: Update AoC Badges
on:
  schedule:                                      # run workflow based on schedule
    - cron: '0 6 1-25 12 *'                      # from the 1. December till 25. December every day at 6am
    
  workflow_dispatch:                             # allow to manually start the workflow 
  
# push:                                          # (disabled) run on push, be carefull with this setting 
                                                 # as the workflow should only be triggered at a rate lower than
                                                 # 4 times a houre to keep traffic on aoc site low 
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
    
      - uses: actions/checkout@v2                # clones your repo, make sure the ssh secret is set!
        with:
          ssh-key: ${{ secrets.SSH_KEY }}
          
      - uses: joblo2213/aoc-badges-action@v2
        with:
          userid: 00000                          # your user id, see setup on how to obtain
          session: ${{ secrets.AOC_SESSION }}    # secret containing session code, see setup on how to obtain
          
#         Optional inputs:
#         
#         leaderboard: 'https://adventofcode.com/2020/leaderboard/private/view/00000.json'               # The url of the leaderboard from witch the data is fetched. Typically your private leaderboard.
#         file: 'README.md'                                                                              # The file that contains the badges
#         dayRegex: '(?<=https:\/\/img\.shields\.io\/badge\/day%20📅-)[0-9]+(?=-blue)'                   # Regular expression that finds the content of the day badge iun your file.
#         starsRegex: '(?<=https:\/\/img\.shields\.io\/badge\/stars%20⭐-)[0-9]+(?=-yellow)'             # Regular expression that finds the content of the stars badge iun your file.
#         daysCompletedRegex: '(?<=https:\/\/img\.shields\.io\/badge\/days%20completed-)[0-9]+(?=-red)'  # Regular expression that finds the content of the days completed badge iun your file.

      - name: Push changes                        # Step that pushes these local changes back to your github repo
        run: |
          git config --global user.email "<>"
          git config --global user.name "aoc-badges-action"
          git add .
          git diff-index --quiet HEAD || git commit --message "Update badges"
          git push
```

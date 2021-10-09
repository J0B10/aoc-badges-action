name: 'AoC-badges'
description: 'Updates the badges of your Readme to show your current Advent of Code stats '
runs:
  using: docker
  image: Dockerfile
inputs:
  session:
    description: >
      Your session code for login. Retrive it from your browser cookies.
      Make sure you use a secret to not leak this to public.
    required: true
  userid:
    description: >
      Your unique userid on adventofcode.com, obtain it from **YOUR** private leaderboard url (its the number at the end of the url).
    required: true
  year:
    description: >
      The year for which the stats should be retrived. 
      If not speified, the current year (from system time) is used.
    required: false
  leaderboard:
    description: >
      The url of your leaderboard json file. 
      You can get it by just appending .json to the url of your leaderboard.
    required: false
  file:
    description: >
      The file where the badges should be updated. Default is README.md
    required: false
    default: 'README.md'
  dayRegex:
    description: >
      A regular expression to find the day badge in your file. Must be changed if you change the badge.
    required: false
    default: '(?<=https:\/\/img\.shields\.io\/badge\/day%20📅-)[0-9]+(?=-blue)'
  starsRegex:
    description: >
      A regular expression to find the stars badge in your file. Must be changed if you change the badge.
    required: false
    default: '(?<=https:\/\/img\.shields\.io\/badge\/stars%20⭐-)[0-9]+(?=-yellow)'
  daysCompletedRegex:
    description: >
      A regular expression to find the completed days badge in your file. Must be changed if you change the badge.
    required: false
    default: '(?<=https:\/\/img\.shields\.io\/badge\/days%20completed-)[0-9]+(?=-red)'
branding:
  icon: 'star'
  color: 'yellow'

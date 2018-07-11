## 0.0.1 - 2018-07-06
### Added
- This CHANGELOG file .
- README now contains first instructions on installation
- Game App urls, views, serializers and models

## 0.0.2 - 2018-07-06
### Added
- Now you can create a game a select the pegs colors
- Guesses list endpoint is available
- Mastemrind algorithm is ready to use

## 0.0.3 - 2018-07-07
### Added
- List every guess in a game when list or detail endpoints are called

## 0.0.4 - 2018-07-08
### Added
- Now we get suggestions after each guess

## 0.0.5 - 2018-07-09
### Change
- Changes on settings in order to allow the personalization of some variables in each enviroment, 
specially ALLOWED_HOSTS
- Now an anonymous user can POST games and guesses

## 0.0.6 - 2018-07-09
### Added
- Now every game closes automatically when the maximum number of tries is reached or when the riddle is solved
- Returns error when trying to guess on a closed game

## 0.0.7 - 2018-07-11
### Added
- Added unittest for the Game and Guesses views and models

# 449wordleproject3

### Group Members:
##### Fenil Ketan Bhimani
##### Charlie Taylor
##### Brent Pfefferle
##### Jarrod Leong

## **Initializing Database, Cron Service & Start Project:**
##### copy 'wordleauth' into your nginx directory (/etc/nginx/sites-enabled/)
##### restart nginx `sudo service nginx restart`
##### setup the Cron service to retry failed jobs
- install run-one `sudo apt install run-one`
- open terminal and type `crontab -e` and then select you choice of editor
- navigate to bottom of file and add the command `*/10 * * * * run-one rq requeue --all --queue default` to retry failed jobs every 10 minutes
- save the file and exit
- you can check if it saved with the command `crontab -l`
###### *cron job was not running properly on Jarrod Leong's system but worked on Brent Pfefferle's system so command should be working*
##### navigate to project directory
##### to setup file structures for litefs database replication, run `python3 setup.py`  *if setup.py fails, manually delete the folder /database/dbs* 
###### *Make sure you have redis installed and it's not running.  you can check with the command `pgrep redis`*
##### run `foreman start` before populating datbases
##### *the leaderboard service will try and register with the game service before starting.  It may take some seconds to register and start the service.*
##### setup the databases by running `python3 setupDB.py`  *use `setupDB.py -p` to populate the database.  Note it resets the redis db as well*
###### *if the project fails to start, delete the dbs folder and run setup again. Check again that redis is not running.  Litefs is included but if the replication services are failing, you may need to redownload Litefs and add it into /src/database/ and try again.*

---

## **Testing the APIs**

#### *Can test using user-id: 123abc and username: user1.  Username is not checked but included for redundancy*
#### *includes games g1 and g2 as test games.  game_ids are shortend here for ease of use but are uuids in game*
#### *make sure to use the correct user-id.  Supplying an incorrect user-id after you have logged in will result in resources not being found as username and user-id will not match. When using /game/create you will be able to create games even with an incorrect user-id but you will not be able to access them.*

### **Register Username & Password**
##### `http POST http://tuffix-vm/register username=<username> password=<password>`

### **Create a Game**
##### `http POST http://tuffix-vm/game/create user-id:<user-id> username:<username> -a <username>:<password>`

### **Input Word Guess**
##### `http POST http://tuffix-vm/game/guess user-id:<user-id> username:<username> game_id=<game_id> guess=<guess> -a <username>:<password>`

### **List All Games in Progress**
##### `http GET http://tuffix-vm/game/list user-id:<user-id> username:<username> -a <username>:<password>`

### **List a Specific Game in Progress**
##### `http GET http://tuffix-vm/game/{game_id} user-id:<user-id> username:<username> -a <username>:<password>`

### **Register service to webhook**
##### `http POST http://tuffix-vm/game/register callback=<url>`

### **Get Leaderboard**
##### `http GET http://tuffix-vm/leaderboard`

### **Update Leaderboard**
##### *Tests that you can update the leaderboard via only internal calls and not external (via tuffix-vm)*
##### `http POST http://tuffix-vm/leaderboard/update username=<username> score=<score>` *SHOULD RETURN 404*
##### `http POST http://localhost:5400/leaderboard/update username=<username> score=<score>` *SHOULD RETURN 200 OK WITH JSON OUTPUT*














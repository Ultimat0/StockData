from flask import Flask, request

auth_key = "Bearer " + input ("Enter your authorization key: ")


"""TODO: 

- Receive authentication key (check - we did it manually)
- inject key into other objects when necessary
- Test if the API is broken or if it just needs an authentication 
  key to work properly (it's not getting any data for certain 
  date ranges) (It's broken - submitted a bug report)
    - submit bug report if API doesn't function properly (check)
- Implement get_fundamentals ()
- Check out Tiingo and intrinio for news

"""
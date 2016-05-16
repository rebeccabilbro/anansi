# anansi
Twitter data ingestion tool, inspired by [Bonzanini's Twitter stream project](https://gist.github.com/bonzanini/af0463b927433c73784d).

![Spider web with dew](figures/web.jpg)

Photo used with permission, [Creative Commons License](https://www.flickr.com/photos/billdamon/9999441844/in/photolist-geBKFJ-78XWAt-8hH7oD-addhzJ-5wrtoF-5wr2sV-78XYzt-fFDTuR-8hvdn3-8KqGNc-8QEkxD-bUGBet-78XXon-r7YuEB-792QzY-f1YBq2-4MX5RR-58Ew3n-5tMEpu-5Txgvn-NDYxe-aTfp7-5pLcJv-2UegpA-jTcuT4-npTgP-5SC8Xu-6ov6LH-3jLSBu-ahyzqV-8hvke1-uQUXQ-8WkHvV-5h9xdK-BpYn-oqFWid-7XgS1k-7gtg7J-xwsCpx-6ur1W9-6zmQc7-a2UQHo-BEhKC-8dFQ3q-78XXSt-5YZuNX-3nwa1-ahyzLv-7eaaA9-6ozkWf)

To use `anansi`:    

```bash
pip install tweepy==3.3.0

git clone https://github.com/CommerceDataService/anansi.git
cd anansi
```

Now go to the [Twitter Developer Hub](https://apps.twitter.com/) and register for an app so that you can get your own consumer key, consumer secret, access token, and access secret.  Save these to your _local_ machine, in a file called config.py inside the anansi repo as such:

consumer_key    = " "    
consumer_secret = " "    
access_token    = " "    
access_secret   = " "    

For your convenience, we've added config.py to the list of files and folders to be ignored (.gitignore) when you push this project to GitHub. This will help keep your keys, tokens, and secrets private for this project. __Note: Do NOT push your API keys, token, or secrets to GitHub or publish them anywhere else!__

Once you have your config.py file set up with all your developer authentication information, go back to the command line and type:

```bash
mkdir data
python anansi.py -q wmata -d data
```
The result will be a list of tweets for the query "wmata" in data/stream_wmata.json. _Hint: you can replace 'wmata' with a search term of your own depending on your topic interest._


## Experiment 1    
 - Ingestion began Thursday, May 12, 2016 at 2:52PM EST    

### Log 1   
 - 675 wmata tweets collected as of Friday, May 13, 2016 at 12:04AM EST    
 - storage: 3,437,721 bytes (3.4 MB on disk)    

### Log 2  
 - 1480 wmata tweets collected as of Friday, May 13, 2016 at 10:42AM EST    
 - storage: 6,997,619 bytes (7 MB on disk)    

### Log 3  
 - 3561 wmata tweets collected as of Saturday, May 14, 2016 at 12:24AM EST     
 - storage: 17,550,666 bytes (17.6 MB on disk)   

### Log 4  
  - 3948 wmata tweets collected as of Saturday, May 14, 2016 at 6:09PM EST         
  - storage: 19,250,900 bytes (19.3 MB on disk)     

### Log 5     
 - 4259 wmata tweets collected as of Sunday, May 15, 2016 at 2:57PM EST    
 - storage: 20,803,748 bytes (20.8 MB on disk)

### Log 6     
- 4634 wmata tweets collected as of Monday, May 16, 2016 at 9:34AM EST   
- storage: 22,449,626 bytes (22.5 MB on disk)


## To Dos
 - target: 1 million tweets    
 - trim JSON to compress storage, aiming for 200MB for full dataset    
 - load tweets from disk to MongoDB/AWS storage    


## Resources
[SNAP lab's research](http://snap.stanford.edu/data/index.html)

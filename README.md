##Line Server Problem - Salsify

1 . How does your system work? (if not addressed in comments in source)
The DocServeApi is a lightweight API impleted with highly optimized framework - falcon api and running on a pypy python interpreter (python's fastest known 
interpreter). 
When the API is started, a redis server is also initialized to handle cache. Similarly, the new file is path is stored.
The file is broken down into many smaller chunks. By doing this, we are minimizing look up-time for a line in a particular file.
The api goes ahead to to not only cache the response for the requested line but also for the preceding lines because of historical nature of users requesting information that 
is either closely related or interlinked intermitently.To minimize I/O performace, we do not load the entire file into memory but instead split the file into chunks in a binary fashion and access the chunks would highly likely
contain the line we are looking for. Each of line lookups are threaded and pooled using python's multiprocessing lib.

2. How will your system perform with a 1 GB file? a 10 GB file? a 100 GB file?
The system will perform at O(nlog(n) with increasing sizes of the file with the implementation of the chunkify that breaks down the file into a binary like tree but breaks out as soon as it gets it’s value. 

3. How will your system perform with 100 users? 10000 users? 1000000 users?
The increasing number of users would increase the number of requests hitting the service. At the moment, i’m asynchronously chunking up the a given file while finding the matching file however as requests increase, the number of multithreaded pools due to the CPU will become bottle a bottle neck. 

4. What documentation, websites, papers, etc did you consult in doing this assignment?
Falcon API, StackOverflow, python.org website, Redis server, python multithreading and multiprocessing.

5. What third-party libraries or other tools does the system use? How did you choose each library or framework you used?
I chose the falcon API over using a simple HTTP server, another framework or another interpreter because research had found the combination of optimization of the api and the interpreter to process over 340,000 requests a second or put backwards, it takes 3 ultra-seconds of processing per request, which is not bad for latency for an API.I started off with the hope of using flask, a well known python API but upon doing research, realized it came with overhead over it’s generic functionality, it would 
be a bottleneck once we began scaling, as a result, i went with falcon. I also chose to use the redis-server for caching instead of a dictionary because it's a highly
distributed system that would make saving and retrieving of cached information easier in the event that this increased exponentially

6. How long did you spend on this exercise? If you had unlimited more time to spend on this, how would you spend it and how would you prioritize each item?
I spent about 5 hours on this piece mainly doing a tonne of planning and research around the anticipated bottlenecks like I/O bound events and CPU events.
I also spent a good majority of the time decoupling many pieces of the code to allow for scalability. 
I would have derived an equation to give me an optimum number of lines to include in each file and files in folders depending on the length or size of the input file. Despite having to load the entire file into memory, i would have an entire binary tree structure that is O(log(n)) which would make indexing a lot faster. In the same spirit, I would have used some of this time to derive another equation to get an optimum number of threads and processes to be used in I/O bound functions.
Similarly, i would have had a separate server taking care of configuration with a custom tool like ZooKeeper to make deployments much more manageable.
I also would have used the same redis server to implement 2 queueing systems, one for the requests coming into the system and the other on the threadUp function with more user requests against the system.
It is always good practice to have very nice documentation for clients and therefore spending time to outline what the parameter lists are, and the expected returns and errors in a more digestible fashion would have paid off. Still on the client-side, fully implementing the full https protocol at minimum or a full token-based handshake could have go long way to protect the API from unscrupulous throttlers. Additionally implementing some kind of rate Limiting function could ensure the clients are honoring the health of the API


7. If you were to critique your code, what would you have to say about it?
Currently, the code is not unittested and therefore does not have full code coverage. However, this code is well structured and easy to be picked up by a anyone but is separated well enough to easily add functionality to it.
This code does not have sufficient logging and does not catch most of the common error cases that it should. I also think separation of many of functions into smaller functions
avails opportunities for both unit testing but also parallelism and asynchronous work.
From the word go, the idea of retrieving data from the text files screams relational database for this kind of text file. However, there are still some applications such 
a service would come in handy especially in retrieveing data from high sequence data that can come in larger batches of 10-15 gig files.



# Assessment

When your project is finished, or as it's in progress if it's helpful, assess your project. Review the [project rubric](http://cs.fablearn.org/courses/cs10/unit00/project/) and then decide how your project should score on each criterion. Write a paragraph for each criterion justifying your assessment with evidence from your code, planning document, and commit messages.

## Criterion A - Knowing, understanding, and computational thinking

**Score: 8/8**

My project demonstrates the following learning claims:
- I can read documentation to use services written by others.
- I understand HTTP communication between clients and servers.
- I effectively use the principles of decomposition and abstraction to make my code more efficient and elegant.

Firstly, I can read documentation to use services written by others. I used an external API to gather data for my bot, proving that I could read documentation to use a service written by others.

Secondly, I understand HTTP communication between clients and servers. In bot_server.py, I have 8 routes for 8 services  (including new_message and the base / route).
I used appropiate HTTP requests to the external API and parsed the HTTP responses into response data that is able to be used in my services. The HTTP responses were formatted into JSON objects, which were then edited and returned the intended result when tested. This is able to be seen in all the different services I created in services.py.
I also have a descriptive error that reports when something goes awry, as seen on line 30 in bot_server.py.

Thirdly, I have effectively used the principles of decomposition and abstraction to make my code more efficient and elegant. I have created 1 module (services.py) that holds all the services, and 1 module (bot_server.py) that takes care of all the routes for the client side. The services are implemented in such a way that the services can be used in both directly through a HTTP request or using the client and client server to run it as well. My services are all parameterized, so if the input is different, the output/end return would be different as well.

Furthermore, I have created and used edge case preventers in my code as well, so if someone intentionally or unintentionally leaves a space, apostrophe or uses capital letters in the wrong place the service will still be able to run as intended. One example of this is if someone is trying to get the title of a champion (Zed for example), and they type title "Z'''   E 'd'", the edge case preventer will modify the string to become "Zed" instead and return the title for Zed. If someone adds numbers or quotations in the client side, this will result in an error that says "A service and champion is required to get results". If someone is intentionally trying to get an error, they will get that, however simple errors such as forgetting a space or using an apostrophe would still return the intended result of the service.
## Criterion B - Planning and development
**Score: 6/8**

My project demonstrates the following learning claims:
- I can thoughtfully plan a large computer science project.
- I can iteratively develop a project using version control tools such as GitHub.
- I can document my software so that it is readable and usable by others.

Firstly, I can thoughtfully plan a large computer science project. From the planning document I used, it is able to be seen that I have planned this computer science project very thoroughly. Although parts of the document aren't fully filled out, the project design and test and use cases are filled out with a lot of detail and describe lots of different use cases and what it would return when that happens. I have also updated the planning document when services had to be modified or added.

Secondly, I can iteratively develop a project using version control tools such as GitHub. Over the course of this project, I have made over 13 descriptive commits to the Github, and I used a stub function to temporarily stand in for some of my services then changed. I have also went from 3 services to 5 services, offering more different data to the user.

Thirdly, I can document my software so that it is readable and usable by others. I used the README.md file to write descriptions of what my services do and also included a table for easy viewing and understanding of what my bot and services do. Aside from this, I also have small lines of documentation that says what each part of a function does, along with a small description of each service in services.py.

In conclusion, even though my planning document still can do with some more detail, I have done very well in other areas of criterion B. This is why I think I demonstrate a 6 in criterion B.

## Criterion C - Evaluation
**Score: 7/8**

My project demonstrates the following learning claims:
- I can identify different scenarios in which my code may be used and outline the expected functionality of my code in these instances.
- I can develop a testing strategy to ensure my code works as expected.

Firstly, I identified different scenarios in which my code may be used and outline the expected functionality of my code in these instances. In the planning document, I have outlined the different scenarios my code may be used in. I have also written the expected values when inputted with both normal use cases and edge cases. Because I have noted down the expected values of both the normal use cases and edge cases, I was able to lessen the amount of edge cases by modifying the inputted string using string modifiers and the particular code is able to be seen in all of the services of service.py. An example would be in line 28 to 39, where the strings are modified in different ways depending on the inputted string.

Secondly, I have developed a testing strategy to ensure my code works as expected. In my planning document, it is able to be seen that I have a detailed testing strategy that tests and makes sure my code works as expected based on all of my use cases and edge cases. Originally before developing edge case preventers, capital letters, random spacing, and  apostrophes all affected the output, making an error when inputted. These can be both intentional or unintentional errors, so I coded the string modifier (AKA edge case preventer) to prevent these symbols and letters from affecting my code. However, I could try to prevent even more edge cases by adding symbols such as !@#$%^&*()-~][]/ and more to prevent intentional and malicious errors from happening.

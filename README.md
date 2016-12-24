# PROJECT-STIRR

Plagiarism is indeed a nagging problem in the world of academia. The individuals that both offer solutions to expose any instances of plagiarism, as well as the individuals that discover ways to get around these solutions, are pretty much the players in what I'd like to refer as a "cat and mouse" game. As methods of counteracting plagiarism improve, methods also improve for the people counteracting these solutions. It's a never ending cycle, and both parties depend on the other to amplify the growth in their skills and abilities.

If you haven't realized it yet, I'm just another mouse, here to help the cat improve his game.

The project I have presented here is an ongoing pursuit in exploiting plagiarism software. Various plagiarism software exists to detect similarities in code structures, however, with the right logic, it is very possible to alter the structure and appearence of code, and still preserve the flow of data and yeild an identical output. This altering of code structure can be achieved by the use of...

# Mechanical Disguise

From what I've tested thus far, changing statements in code to their alternaitive representations essentially "changes" the structure but preserves information. Doing certain tweaks such as changing for loops to while loops, changing a >= b into a > b && a == b, etc. is a process known as mechanical disguises and can be used to confuse the plagiarism detectors and have your code seen as "legitimate" and "original". More on this subject can be found through this link: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.150.1594&rep=rep1&type=pdf

The initial goal is to create code that can automate this process of mechanically disguising every part of your source code, by mapping each statement with their alternative one. However, if multiple students were to use a program that conducted such automation, everyones code would look the same, assuming they are using the same source code to obfuscate from. Which is why, to counteract this problem, I plan to not only automate this process of mechanically disguising code, but also ensure that every output created by this program is random as well. Given that programming languages offer various methods in representing logic in code, it is possible to devise algorithms that can randomly change certain statements and still preserve the outright logic. 

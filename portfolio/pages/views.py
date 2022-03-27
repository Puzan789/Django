from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context  = {
    'title': '  Hi, I am puzan',
    'para1':'I am currently studying  python and django as well as programming language. I learn to make  websites and webapplications using python, django, html, css andjavascript,react.',
    'para2':'''As a programming student  I am eager to learn python, django, javascript
                programming. Feel free to check out some of my
                blogs, at my blog page.''',
    'skills_list':'  HTML,CSS,Bootstrap,Javascript,jQuery,Git,Github,Python,',
    'softwares_list':'VsCode,Chrome,Firefox,Linux, Fedora, Postman,etc',
    'mail':'puzan8516@gmail.com',
     }
    return render(request, "pages/index.html",context)

    

def contact(request):
    return render(request, "pages/contact.html")

def blog(request):
    blogs_list = [

        {   'id':1,
            'title':'PYTHON',
            'subtitle':'''Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.
                                    Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library''',
            'date':'15 mar 2022',
            'image':'img/python.jpg',
            'btntext':'Read more about this blog.↗',
            'paragraph':'''Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.[29]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard libraryOften, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective. ''',
        },
        {
            'id':2,
            'title':'Javascript',
            'date':'15 Mar 2022',
            'subtitle':''' javaScript is a programming language for the web. Its syntax is based on Java and C languages. Used in both the front-end and back-end of many platforms, JavaScript has become a standard. For every animated or interactive object you see online, chances are JavaScript is involved.
                                JavaScript’s language is widely used to create a more interactive front-end. Still, it is used in competition with other languages to create web scrapers, servers, and many other tools. This is because of the language and design decisions made when creating the language.
                                According to the 2020 Stack Overflow Developer Survey , JavaScript is the most popular coding language.''',
            'image':'img/jva.jpg',
            'btntext':'Read more about this blog.↗',
            'paragraph': '''JavaScript and Java are similar in some ways but fundamentally different in some others. The JavaScript language resembles Java but does not have Java's static typing and strong type checking. JavaScript follows most Java expression syntax, naming conventions and basic control-flow constructs which was the reason why it was renamed from LiveScript to JavaScript.
                                In contrast to Java's compile-time system of classses built by declarations, JavaScript supports a runtime system based on a small number of data types representing numeric, Boolean, and string values. JavaScript has a prototype-based object model instead of the more common class-based object model. The prototype-based model provides dynamic inheritance; that is, what is inherited can vary for individual objects. JavaScript also supports functions without any special declarative requirements. Functions can be properties of objects, executing as loosely typed methods.
                        JavaScript is a very free-form language compared to Java. You do not have to declare all variables, classes, and methods. You do not have to be concerned with whether methods are public, private, or protected, and you do not have to implement interfaces. Variables, parameters, and function return types are not explicitly typed. JavaScript and Java are similar in some ways but fundamentally different in some others. The JavaScript language resembles Java but does not have Java's static typing and strong type checking. JavaScript follows most Java expression syntax, naming conventions and basic control-flow constructs which was the reason why it was renamed from LiveScript to JavaScript.
                        In contrast to Java's compile-time system of classes built by declarations, JavaScript supports a runtime system based on a small number of data types representing numeric, Boolean, and string values. JavaScript has a prototype-based object model instead of the more common class-based object model. The prototype-based model provides dynamic inheritance; that is, what is inherited can vary for individual objects. JavaScript also supports functions without any special declarative requirements. Functions can be properties of objects, executing as loosely typed method.
                        JavaScript is a very free-form language compared to Java. You do not have to declare all variables, classes, and methods. You do not have to be concerned with whether methods are public, private, or protected, and you do not have to implement interfaces. Variables, parameters, and function return types are not explicitly typed.''',
                        },
        {
            'id':3,
            'title':'c++',
            'subtitle':'  C++ is a programming language developed by Bjarne Stroustrup in 1979 at Bell Labs. C++ is regarded as a middle-level language, as it comprises a combination of both high-level and low-level language features. It is a superset of C, and that virtually any legal C program is a legal C++ program. C++ runs on a variety of platforms, such as Windows, Mac OS, and the various versions of UNIX.',
            'date':' 15 mar 2022',
            'image':'img/c.png',
            'btntext':'Read more about this blog.↗',
            'paragraph':' Since its creation, C++ has become one of the most widely used programming languages in the world. Well-written C++ programs are fast and efficient. The language is more flexible than other languages: It can work at the highest levels of abstraction, and down at the level of the silicon. C++ supplies highly optimized standard libraries. It enables access to low-level hardware features, to maximize speed and minimize memory requirements. C++ can create almost any kind of program: Games, device drivers, HPC, cloud, desktop, embedded, and mobile apps, and much more. Even libraries and compilers for other programming languages get written in C++. One of the original requirements for C++ was backward compatibility with the C language. As a result, C++ has always permitted C-style programming, with raw pointers, arrays, null-terminated character strings, and other features. They may enable great performance, but can also spawn bugs and complexity. The evolution of C++ has emphasized features that greatly reduce the need to use C-style idioms. The old C-programming facilities are still there when you need them. However, in modern C++ code you should need them less and less. Modern C++ code is simpler, safer, more elegant, and still as fast as ever',
            }
    ]
    cont = {
        'blogs_list':blogs_list,
    }
    return render(request, "blogs/blogs.html",cont)

def blog_detail(request,id):
    blogs_list = [
        {   'id':1,
            'title':'PYTHON',
            'subtitle':'''Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.
                                    Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library''',
            'date':'15 mar 2022',
            'image':'img/python.jpg',
            'btntext':'Read more about this blog.↗',
            'paragraph':''' Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.[29] Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library

"Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed. Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.

Dating from 1991, the Python programming language was considered a gap-filler, a way to write scripts that “automate the boring stuff” (as one popular book on learning Python put it) or to rapidly prototype applications that will be implemented in other languages. However, over the past few years, Python has emerged as a first-class citizen in modern software development, infrastructure management, and data analysis. It is no longer a back-room utility language, but a major force in web application creation and systems management, and a key driver of the explosion in big data analytics and machine intelligence.

n Python, everything in the language is an object, including Python modules and libraries themselves. This lets Python work as a highly efficient code generator, making it possible to write applications that manipulate their own functions and have the kind of extensibility that would be difficult or impossible to pull off in other languages. Python can also be used to drive code-generation systems, such as LLVM, to efficiently create code in other languages.'''
},
         {
            'id':2,
            'title':'Javascript',
            'subtitle':''' javaScript is a programming language for the web. Its syntax is based on Java and C languages. Used in both the front-end and back-end of many platforms, JavaScript has become a standard. For every animated or interactive object you see online, chances are JavaScript is involved.
                                JavaScript’s language is widely used to create a more interactive front-end. Still, it is used in competition with other languages to create web scrapers, servers, and many other tools. This is because of the language and design decisions made when creating the language.
                                According to the 2020 Stack Overflow Developer Survey , JavaScript is the most popular coding language.''',
            'date':'15 Mar 2022',
            'image':'img/jva.jpg',
            'btntext':'Read more about this blog.↗',
            'paragraph':''' avaScript is a programming language for the web. Its syntax is based on Java and C languages. Used in both the front-end and back-end of many platforms, JavaScript has become a standard. For every animated or interactive object you see online, chances are JavaScript is involved. JavaScript’s language is widely used to create a more interactive front-end. Still, it is used in competition with other languages to create web scrapers, servers, and many other tools. This is because of the language and design decisions made when creating the language. According to the 2020 Stack Overflow Developer Survey , JavaScript is the most popular coding language.


JavaScript and Java are similar in some ways but fundamentally different in some others. The JavaScript language resembles Java but does not have Java's static typing and strong type checking. JavaScript follows most Java expression syntax, naming conventions and basic control-flow constructs which was the reason why it was renamed from LiveScript to JavaScript. In contrast to Java's compile-time system of classes built by declarations, JavaScript supports a runtime system based on a small number of data types representing numeric, Boolean, and string values. JavaScript has a prototype-based object model instead of the more common class-based object model. The prototype-based model provides dynamic inheritance; that is, what is inherited can vary for individual objects. JavaScript also supports functions without any special declarative requirements. Functions can be properties of objects, executing as loosely typed methods. JavaScript is a very free-form language compared to Java. You do not have to declare all variables, classes, and methods. You do not have to be concerned with whether methods are public, private, or protected, and you do not have to implement interfaces. Variables, parameters, and function return types are not explicitly typed.

Java is a class-based programming language designed for fast execution and type safety. Type safety means, for instance, that you can't cast a Java integer into an object reference or access private memory by corrupting the Java bytecode. Java's class-based model means that programs consist exclusively of classes and their methods. Java's class inheritance and strong typing generally require tightly coupled object hierarchies. These requirements make Java programming more complex than JavaScript programming. In contrast, JavaScript descends in spirit from a line of smaller, dynamically typed languages such as HyperTalk and dBASE. These scripting languages offer programming tools to a much wider audience because of their easier syntax, specialized built-in functionality, and minimal requirements for object creation.
'''

        },
        {
            'id':3,
            'title':'c++',
            'subtitle':'C++ is a programming language developed by Bjarne Stroustrup in 1979 at Bell Labs. C++ is regarded as a middle-level language, as it comprises a combination of both high-level and low-level language features. It is a superset of C, and that virtually any legal C program is a legal C++ program. C++ runs on a variety of platforms, such as Windows, Mac OS, and the various versions of UNIX.',
            'date':'15 mar 2022',
            'image':'img/c.png',
            'btntext':'Read more about this blog.↗',
            'paragraph':''' C++ is a programming language developed by Bjarne Stroustrup in 1979 at Bell Labs. C++ is regarded as a middle-level language, as it comprises a combination of both high-level and low-level language features. It is a superset of C, and that virtually any legal C program is a legal C++ program. C++ runs on a variety of platforms, such as Windows, Mac OS, and the various versions of UNIX.
15 Feb 2022

Since its creation, C++ has become one of the most widely used programming languages in the world. Well-written C++ programs are fast and efficient. The language is more flexible than other languages: It can work at the highest levels of abstraction, and down at the level of the silicon. C++ supplies highly optimized standard libraries. It enables access to low-level hardware features, to maximize speed and minimize memory requirements. C++ can create almost any kind of program: Games, device drivers, HPC, cloud, desktop, embedded, and mobile apps, and much more. Even libraries and compilers for other programming languages get written in C++.

One of the original requirements for C++ was backward compatibility with the C language. As a result, C++ has always permitted C-style programming, with raw pointers, arrays, null-terminated character strings, and other features. They may enable great performance, but can also spawn bugs and complexity. The evolution of C++ has emphasized features that greatly reduce the need to use C-style idioms. The old C-programming facilities are still there when you need them. However, in modern C++ code you should need them less and less. Modern C++ code is simpler, safer, more elegant, and still as fast as ever.

The following sections provide an overview of the main features of modern C++. Unless noted otherwise, the features listed here are available in C++11 and later. In the Microsoft C++ compiler, you can set the /std compiler option to specify which version of the standard to use for your project.
'''

        },
        
    ]

    for blog in blogs_list:
        if blog['id'] == int(id):
            context = {
                'blog':blog,
            }
    return render(request, "blogs/blog_detail.html",context)



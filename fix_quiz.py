#!/usr/bin/env python3
"""Generate complete HTML replacement for Q69-Q131 with shuffled answers."""

import random
import json
import re

# The original question data with explanations
original_data = {
    69: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "According to IEEE, a requirement is defined as:",
        "exp": "IEEE defines a requirement as: (1) a condition or capability needed by a user to solve a problem or achieve an objective, and (2) a condition or capability that must be met by a system to satisfy a contract, standard or specification.",
        "opts": ["A deployment script","A test case for the system","A line of code in the system","A conditional capability needed by a user to solve a problem or achieve an objective"]
    },
    70: {"keep": True},  # Keep as is - has ans:1 which is better
    71: {"keep": True},  # Keep as is - has ans:1 which is better
    72: {"keep": True},  # Keep as is - has ans:1 which is better
    73: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "What are the FOUR main activities in the requirements engineering process?",
        "exp": "The four main RE activities are: (1) Feasibility Study, (2) Requirements Elicitation & Analysis, (3) Requirements Specification, (4) Requirements Validation.",
        "opts": ["Interviews, scenarios, use cases, and prototypes","Planning, design, coding, and testing","Coding, testing, deployment, and maintenance","Feasibility, elicitation, specification, and validation"]
    },
    74: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "The purpose of a Feasibility Study is to:",
        "exp": "A feasibility study estimates whether identified user needs can be satisfied using current software and hardware technologies, and considers whether the system is cost-effective within budgetary constraints.",
        "opts": ["Release the system to production environment","Execute test cases on the software","Document and write the SRS paper","Assess if needs can be satisfied cost-effectively"]
    },
    75: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "Requirements Elicitation involves:",
        "exp": "Requirements elicitation and analysis is the process of deriving system requirements through observation of existing systems, discussions with potential users and procurers, task analysis, and development of prototypes.",
        "opts": ["Executing unit tests on source code","Deploying and releasing the software","Writing code based on developer guesses","Deriving requirements through observation and discussion"]
    },
    76: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "Which property of a good SRS means it should only specify WHAT and not HOW?",
        "exp": "The 'black-box view' property means the SRS should specify the external behavior of the system without discussing implementation. The SRS views the system as a black box.",
        "opts": ["Structured","Verifiable","Concise","Black-box view"]
    },
    77: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "Which SRS property means all requirements must be measurable and checkable?",
        "exp": "Verifiable means all requirements in the SRS document should be verifiable — it should be possible to determine whether or not requirements have been met in an implementation.",
        "opts": ["Conceptual Integrity","Structured","Concise","Verifiable"]
    },
    78: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "Functional requirements must be:",
        "exp": "Functional requirements specification should be Complete (all services required by the user defined) and Consistent (no contradictory definitions or ambiguity).",
        "opts": ["Only about security","Only about performance","Vague and flexible","Complete and Consistent (no contradictions)"]
    },
    79: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "Non-functional requirements typically relate to:",
        "exp": "Non-functional requirements are not concerned with specific services but constrain characteristics of the system as a whole — like performance, security, or availability. They can be deciding factors for system survival.",
        "opts": ["Only user interface presentation aspects","Only database schema and storage","Specific system features like login modules","Quality attributes affecting the entire system"]
    },
    80: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "Requirements Validation checks requirements for:",
        "exp": "During requirements validation, checks include: Validity, Consistency, Completeness, Realism and Verifiability. Fixing a requirements error after delivery can cost up to 100x more than fixing an implementation error.",
        "opts": ["Meeting system performance benchmarks","System readiness for deployment phase","Source code quality and structure standards","Validity, consistency, completeness, realism"]
    },
    81: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "Which requirements validation technique involves developing an executable model to show to users?",
        "exp": "Prototyping involves developing an executable model of a system and using it with end-users and customers to see if it meets their needs. Stakeholders experiment with the system and provide feedback.",
        "opts": ["Automated consistency analysis","Test-case generation","Reviews","Prototyping"]
    },
    82: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "In requirements elicitation, 'Ethnography' means:",
        "exp": "Ethnography involves a social scientist spending considerable time observing and analysing how people actually work. People do not have to explain their work — social and organisational factors are directly observed.",
        "opts": ["Making prototypes of the proposed system","Writing formal use case documents","Conducting structured interview sessions","Observing and analyzing how people actually work"]
    },
    83: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "In Use Cases, an 'Actor' is defined as:",
        "exp": "An Actor is a person or a system which uses the system being built for achieving some goal. In use case diagrams, actors are represented as stick figures.",
        "opts": ["A database table record","A pre-written test case","Only the system administrator","A person or system using the system being built"]
    },
    84: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "What does the 'Main Success Scenario' in a Use Case describe?",
        "exp": "The Main Success Scenario describes the interaction if nothing fails and all steps in the scenario succeed — the ideal, happy-path flow.",
        "opts": ["Performance measurements under system load","Alternative paths when errors occur","What happens if the system crashes","Ideal flow when everything succeeds"]
    },
    85: {
        "topic": "Requirements Analysis",
        "topicColor": "#a78bfa",
        "q": "Which activity in requirements elicitation deals with resolving conflicts between stakeholders?",
        "exp": "Requirements Prioritization and Negotiation is concerned with prioritizing requirements and finding/resolving conflicts through negotiation when multiple stakeholders are involved.",
        "opts": ["Requirement specification and documentation","Requirement classification and organization","Requirements discovery and gathering","Requirements prioritization and negotiation"]
    },
    86: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "Software design is best defined as:",
        "exp": "Software design is a process of transforming user requirements into a suitable form which helps the programmer in software coding and implementation.",
        "opts": ["Testing software thoroughly before release","Deploying software to production environment","Writing and coding the source code","Transforming requirements into suitable form"]
    },
    87: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "Which type of software runs on a local computer and includes all functionality without a network?",
        "exp": "Stand-alone Applications are application systems that run on a local computer (such as a PC). They include all necessary functionality and do not need to be connected to a network.",
        "opts": ["Systems processing data in batches","Systems that control embedded devices","Applications accessed via the internet","Applications running on a local computer"]
    },
    88: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "Embedded Control Systems are:",
        "exp": "Embedded Control Systems are software control systems that control and manage hardware devices. Numerically, there are probably more embedded systems than any other type of system.",
        "opts": ["Systems that process data in batches","Software for entertainment purposes","Applications accessed on the web","Software systems controlling hardware devices"]
    },
    89: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "The FIRST activity in the software design process is:",
        "exp": "Architectural Design is the highest abstract version of the system — the first design activity. It identifies software as a system with many interacting components and establishes the sub-system framework.",
        "opts": ["Database design and schema creation","Component design and implementation","Interface design and specification","Architectural design of the system"]
    },
    90: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "Architectural Design output is:",
        "exp": "The output of the architectural design is an Architectural Design Document (System Architecture) describing sub-systems and their control and communication frameworks.",
        "opts": ["A fully deployed application system","Automated test cases for validation","Compiled source code and executables","Design document describing system architecture"]
    },
    91: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "Interface Design in software design involves:",
        "exp": "Interface Design defines the interfaces between system components. This specification must be unambiguous — with precise interfaces, components can be designed and developed concurrently.",
        "opts": ["Writing automated test cases and scripts","Creating database tables and schemas","Writing the user interface code only","Specifying interfaces between system components"]
    },
    92: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "Database Design in software design involves:",
        "exp": "Database Design involves designing the system data structures and how these are to be represented in a database — either reusing an existing database or creating a new one.",
        "opts": ["Testing database server performance loads","Deploying database to production servers","Writing SQL queries for data access","Designing data structures and database schema"]
    },
    93: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "An IDE (Integrated Development Environment) is:",
        "exp": "An IDE is an environment where processes and tools are coordinated to provide developers an orderly interface and convenient view of the development process — covering writing code, testing, and packaging.",
        "opts": ["A specialized testing framework only","A platform for deploying software","A database management system only","Environment coordinating tools for development"]
    },
    94: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "Which of the following is an example of an IDE?",
        "exp": "Examples of IDE software include: Eclipse, Microsoft Visual Studio, NetBeans, Xcode, Code::Blocks, Microsoft Visual C++, and Aptana Studio.",
        "opts": ["Google Chrome web browser application","Adobe Photoshop image editing software","Microsoft Word document processor","Eclipse, Visual Studio, or NetBeans"]
    },
    95: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "CASE stands for:",
        "exp": "CASE stands for Computer-Assisted Software Engineering — a set of tools and practices that facilitate management of a software development project.",
        "opts": ["Computer Analysis and System Evaluation","Coding and Software Engineering concepts","Complete Application Software Environment","Computer Aided Software Engineering"]
    },
    96: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "CASE Workbenches are:",
        "exp": "CASE workbenches are collections of integrated tools which support a specific software life cycle stage — e.g. analysis & design, programming, and testing workbenches.",
        "opts": ["Specialized testing tools only","Only software design and modeling tools","Physical desks or tables for developers","Integrated tools supporting development stages"]
    },
    97: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "An 'Open' CASE workbench means:",
        "exp": "An open (public) CASE workbench allows users to add their own tools. New specialist tools can be added, outputs can be used by other systems, and different tool vendors can be used.",
        "opts": ["Only for open-source software projects","Workbench includes no tools by default","The workbench is free and has no cost","Users can integrate their own custom tools"]
    },
    98: {
        "topic": "Software Design",
        "topicColor": "#f472b6",
        "q": "Which tool in a Programming Workbench translates source code into machine code?",
        "exp": "A Language Compiler translates source code into machine/object code. It is one of the key tools in a programming workbench alongside the linker, loader, debugger, and static/dynamic analyzers.",
        "opts": ["Tool that analyzes code at runtime","Static analysis and checking tool","Combines object files into executable","Language compiler that creates object code"]
    },
    99: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "Verification in software testing answers the question:",
        "exp": "Verification asks: 'Have we built the product right?' and 'Does the product meet system specifications?' — checking internal correctness against specifications.",
        "opts": ["Is the software deployed correctly?","Does the product meet user expectations?","Have we built the right product?","Have we built it right per specifications?"]
    },
    100: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "Validation in software testing answers the question:",
        "exp": "Validation asks: 'Have we built the right product?' and 'Does the product meet user expectations?' — checking that what was built is what the customer actually wanted.",
        "opts": ["Does the code follow structure conventions?","Have we built it right per specifications?","Does the product meet system specifications?","Have we built the RIGHT product needed?"]
    },
    101: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "A software 'Defect' is:",
        "exp": "A Defect is a variance from a desired product attribute. Anything that may cause customer dissatisfaction is a defect — whether in system specifications or in the software product itself.",
        "opts": ["A violation of coding style conventions","A timeout or network connection problem","A feature requested but not implemented","Any variance from attributes causing dissatisfaction"]
    },
    102: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "A software 'Fault' is:",
        "exp": "A Fault (also called a bug or defect) is a condition that causes a system to fail in performing its required function. It is the basic reason for software malfunction.",
        "opts": ["A requirement missing from documentation","A temporary network connection timeout","A user bug report or complaint","A condition causing system failure to perform"]
    },
    103: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "A software 'Failure' is:",
        "exp": "A Failure is the inability of a system or component to perform a required function according to its specifications. A failure occurs when software behavior differs from specified behavior.",
        "opts": ["A missing or absent test case","An error in the design documentation","A fault or bug in the source code","System inability to perform per specification"]
    },
    104: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "Validation Testing is:",
        "exp": "Validation testing expects the system to perform correctly using test cases that reflect the system's expected use — demonstrating that the software meets its requirements.",
        "opts": ["Testing focused on finding and exposing defects","Testing security and penetration vulnerabilities","Testing performance under heavy system load","Testing with expected normal usage scenarios"]
    },
    105: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "Defect Testing is:",
        "exp": "Defect testing uses test cases designed to expose defects. The test cases can be deliberately obscure and need not reflect how the system is normally used.",
        "opts": ["User acceptance testing of normal scenarios","Testing using typical expected user patterns","Performance load testing of the system","Testing with deliberately obscure cases"]
    },
    106: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "Integration Testing focuses on:",
        "exp": "Integration testing focuses on whether modules can be integrated properly, with emphasis on testing interfaces between modules. This activity can be considered testing the design.",
        "opts": ["Validating the entire system end-to-end","Testing individual module functionality","User acceptance and satisfaction testing","Testing module integration and interfaces"]
    },
    107: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "Acceptance Testing is also called:",
        "exp": "Acceptance testing is sometimes called 'alpha testing' for custom systems. It tests if the system satisfactorily solves the problems for which it was commissioned. 'Beta testing' is used for software products.",
        "opts": ["Regression testing","Unit testing","Beta testing always","Alpha testing — for custom systems developed for a single client"]
    },
    108: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "Regression Testing is performed when:",
        "exp": "Regression Testing is performed when changes are made to an existing system, to ensure that modifications have not had any undesired side effect of making earlier services faulty.",
        "opts": ["Database schema or structure is updated","A completely new project is initiated","Source code is first being written","Changes are made to check for side effects"]
    },
    109: {
        "topic": "Software Testing",
        "topicColor": "#34d399",
        "q": "The objective of software testing is to:",
        "exp": "The goal of testing is to expose latent defects. Testing cannot show the absence of a defect — it only increases your confidence. Exhaustive testing is impossible due to cost and resources.",
        "opts": ["Teach end users how to use the system","Create user and system documentation","Prove the software has no possible defects","Expose defects before production use"]
    },
    110: {
        "topic": "Evolution & Legacy",
        "topicColor": "#fb923c",
        "q": "Legacy systems are:",
        "exp": "Legacy systems are older systems that rely on languages and technology no longer used for new systems development. They have typically been maintained over a long period and their structure may be degraded.",
        "opts": ["Mobile applications running on devices","Systems exclusively used by government","New systems built with latest technology","Older systems using outdated technology"]
    },
    111: {
        "topic": "Evolution & Legacy",
        "topicColor": "#fb923c",
        "q": "Which is NOT a logical part of a legacy system?",
        "exp": "The logical parts of a legacy system include: System Hardware, Support Software, Application Software, Application Data, Business Processes, and Business Policies and Rules. Cloud APIs are not legacy components.",
        "opts": ["The application data storage","Support software and utilities","System hardware and infrastructure","Cloud API endpoints and services"]
    },
    112: {
        "topic": "Evolution & Legacy",
        "topicColor": "#fb923c",
        "q": "Software Evolution is necessary because:",
        "exp": "Large software systems have long lifetimes. Business changes, new user expectations, hardware/software platform changes, and errors all require software to evolve continuously.",
        "opts": ["Deployment always requires evolution","Software systems never require any changes","Developers enjoy rewriting code from scratch","Business changes generate new requirements"]
    },
    113: {
        "topic": "Evolution & Legacy",
        "topicColor": "#fb923c",
        "q": "'Fault repairs' in software maintenance refers to:",
        "exp": "Fault repairs fix bugs and vulnerabilities. Coding errors are cheapest to fix; design errors are more expensive; requirements errors are the most expensive as extensive system redesign may be necessary.",
        "opts": ["Improving system performance metrics","Adapting to new operating systems","Adding new features to the system","Fixing bugs, vulnerabilities, and errors"]
    },
    114: {
        "topic": "Evolution & Legacy",
        "topicColor": "#fb923c",
        "q": "'Environmental adaptation' maintenance means:",
        "exp": "Environmental adaptation adapts the software to new platforms and environments — required when the hardware, operating system, or other support software changes.",
        "opts": ["Testing software system components","Introducing and adding new features","Fixing and repairing bugs","Adapting software to new platforms or OS"]
    },
    115: {
        "topic": "Evolution & Legacy",
        "topicColor": "#fb923c",
        "q": "Software Reengineering is different from replacement because:",
        "exp": "Reengineering offers Reduced Risk (no high-risk redevelopment) and Reduced Cost (significantly less than developing new software) compared to replacing a legacy system entirely.",
        "opts": ["It requires rewriting all the code","It develops entirely new functionality","Complete reengineering is always faster","Reduces risk and cost compared to replacement"]
    },
    116: {
        "topic": "Evolution & Legacy",
        "topicColor": "#fb923c",
        "q": "'Reverse Engineering' in software reengineering means:",
        "exp": "Reverse Engineering analyzes the program and extracts information from it to help document its organization and functionality. This process is usually completely automated.",
        "opts": ["Converting legacy database structures","Refactoring program code structure","Translating code between programming languages","Analyzing code to document organization"]
    },
    117: {
        "topic": "Evolution & Legacy",
        "topicColor": "#fb923c",
        "q": "'Source Code Translation' in reengineering means:",
        "exp": "Source Code Translation uses a translation tool to convert the program from an old programming language to a more modern version of the same language or to a different language entirely.",
        "opts": ["Cleaning and organizing database files","Improving the overall program structure","Analyzing and documenting code","Converting code to a newer language"]
    },
    118: {
        "topic": "Project Management",
        "topicColor": "#60a5fa",
        "q": "Why is software project management particularly challenging?",
        "exp": "Software management is challenging because: the product is intangible (can't be seen), large projects are unique 'one-off' projects, and software processes are variable and organization-specific.",
        "opts": ["Because software testing is simple","Because there are too many developers","Because software development is inexpensive","Because software is intangible and unique"]
    },
    119: {
        "topic": "Project Management",
        "topicColor": "#60a5fa",
        "q": "Project Risk affects:",
        "exp": "Project Risk affects the project schedule or resources. Example: loss of an experienced system architect delays the design phase.",
        "opts": ["The overall business market conditions","User and customer satisfaction factors","Only the software code quality","The project schedule or resources"]
    },
    120: {
        "topic": "Project Management",
        "topicColor": "#60a5fa",
        "q": "Product Risk affects:",
        "exp": "Product Risk affects the quality or performance of the software being developed. Example: a purchased component failing to perform as expected, causing the system to be slower than expected.",
        "opts": ["Individual team member morale","The organization's financial situation","Only the overall project timeline","The software quality or performance"]
    },
    121: {
        "topic": "Project Management",
        "topicColor": "#60a5fa",
        "q": "Business Risk affects:",
        "exp": "Business Risk affects the organization developing or procuring the software. Example: a competitor introducing a new product may make assumptions about sales of existing software overly optimistic.",
        "opts": ["Individual developer work performance","Only the project timeline and schedule","Only the system code quality","The organization developing the software"]
    },
    122: {
        "topic": "Project Management",
        "topicColor": "#60a5fa",
        "q": "The FOUR steps in the Risk Management Process are:",
        "exp": "The risk management process involves: (1) Risk Identification, (2) Risk Analysis, (3) Risk Planning, (4) Risk Monitoring.",
        "opts": ["Budget, Schedule, Staff, Implementation","Deploy, Monitor, Fix, Document","Plan, Design, Code, Test","Identify, Analyze, Plan, Monitor"]
    },
    123: {
        "topic": "Project Management",
        "topicColor": "#60a5fa",
        "q": "Risk Monitoring involves:",
        "exp": "Risk Monitoring is the process of regularly checking whether assumptions about product, process, and business risks have changed — assessing whether risks are becoming more or less probable.",
        "opts": ["Preventing or eliminating all risks","Finding and identifying new risks only","Writing down the risk management plan","Checking if risk probability or effects change"]
    },
    124: {
        "topic": "Project Management",
        "topicColor": "#60a5fa",
        "q": "Which project management activity involves writing proposals to win contracts?",
        "exp": "Proposal Writing involves writing a proposal to win a contract — describing project objectives, how it will be carried out, cost/schedule estimates, and why the contract should be awarded to the organization.",
        "opts": ["Status reporting and documentation","Human resources and team management","Risk identification and monitoring","Proposal writing to win contracts"]
    },
    125: {
        "topic": "Software Quality",
        "topicColor": "#e879f9",
        "q": "Software Quality can be ensured through:",
        "exp": "Software quality involves two approaches: (1) Measuring attributes of developed software — quality control, and (2) Monitoring and controlling the development process — quality assurance.",
        "opts": ["Purchasing new hardware equipment","Hiring more developers for the team","Writing as much code as possible","Quality control and quality assurance"]
    },
    126: {
        "topic": "Software Quality",
        "topicColor": "#e879f9",
        "q": "Which quality factor refers to meeting specification and users' requirements?",
        "exp": "Correctness is the extent to which software meets its specification and meets its users' requirements — the most fundamental quality factor.",
        "opts": ["Portability across platforms","Usability and ease of interface","System reliability and uptime","Correctness of implementation"]
    },
    127: {
        "topic": "Software Quality",
        "topicColor": "#e879f9",
        "q": "'Maintainability' as a quality factor refers to:",
        "exp": "Maintainability is the effort required to find and fix a fault in the software — a key quality factor for long-term software success.",
        "opts": ["How easily the system can be deployed","How fast the software performance is","How simple the user interface is","The effort to find and fix a fault"]
    },
    128: {
        "topic": "Software Quality",
        "topicColor": "#e879f9",
        "q": "'Portability' as a software quality factor means:",
        "exp": "Portability is the effort required to transfer the software to a different hardware and/or software platform — important for cross-platform software.",
        "opts": ["The software is developed open source","The software works without internet","The software size is small","The effort to transfer software to other platforms"]
    },
    129: {
        "topic": "Software Quality",
        "topicColor": "#e879f9",
        "q": "A 'Quality Plan' in Software QA describes:",
        "exp": "A quality plan describes a number of quality controls — activities that check the project's quality factors are being achieved and produce documentary evidence available to anyone with an interest in quality assurance.",
        "opts": ["The software deployment procedures","Only the coding and style standards","The project budget and timeline","Quality controls and activities to verify quality"]
    },
    130: {
        "topic": "Software Quality",
        "topicColor": "#e879f9",
        "q": "In Software QA, a 'Standard' defines:",
        "exp": "A standard defines a range, limit, tolerance or norm of some measurable attribute against which compliance can be judged. Example: during white box testing, every source code statement must be executed at least once.",
        "opts": ["The organizational team structure","The project timeline and schedule","Rules prescribing how to do something","A measurable attribute norm for compliance"]
    },
    131: {
        "topic": "Software Quality",
        "topicColor": "#e879f9",
        "q": "'Interoperability' as a software quality factor refers to:",
        "exp": "Interoperability is the effort required to make the software work in conjunction with some other software — important for integrated enterprise systems.",
        "opts": ["How easy the system is to use","How secure the software system is","How fast the system performance is","The effort to work with other software"]
    }
}

# Read the shuffled answers from SHUFFLED_QUESTIONS.js
shuffled_answers = {}
with open('SHUFFLED_QUESTIONS.js', 'r') as f:
    for line in f:
        match = re.search(r'{ id:(\d+),.*opts:\[(.*?)\], ans:(\d)', line)
        if match:
            qid = int(match.group(1))
            opts_str = match.group(2)
            new_ans = int(match.group(3))
            # Parse options from the string
            opts = json.loads('[' + opts_str + ']')
            shuffled_answers[qid] = {
                'opts': opts,
                'ans': new_ans
            }

print(f"Loaded {len(shuffled_answers)} shuffled answer sets")

# Generate the HTML replacement code
html_lines = []

for qid in range(69, 132):
    if qid not in original_data:
        continue
    
    data = original_data[qid]
    
    if "keep" in data and data["keep"]:
        # These questions keep their original structure
        print(f"Skipping Q{qid} - keeping original")
        continue
    
    if qid not in shuffled_answers:
        print(f"Warning: Q{qid} not in shuffled answers")
        continue
    
    shuffled = shuffled_answers[qid]
    opts_list = shuffled['opts']
    new_ans = shuffled['ans']
    
    # Format options for HTML
    opts_formatted = ','.join([f'"{opt}"' for opt in opts_list])
    
    # Build the HTML line
    line = f'  {{ id:{qid}, topic:"{data["topic"]}", topicColor:"{data["topicColor"]}",\n'
    line += f'    q:"{data["q"]}",\n'
    line += f'    opts:[{opts_formatted}],\n'
    line += f'    ans:{new_ans}, exp:"{data["exp"]}" }},\n'
    html_lines.append(line)

# Write output
output = ''.join(html_lines)
with open('FIXED_Q69_Q131.txt', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"\n✓ Generated {len(html_lines)} fixed questions")
print("✓ Output written to FIXED_Q69_Q131.txt")
print("\nNow copy the contents of FIXED_Q69_Q131.txt and replace Q69-Q131 in index.html")

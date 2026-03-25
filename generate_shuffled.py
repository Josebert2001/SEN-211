#!/usr/bin/env python3
"""Generate shuffled questions Q69-Q131 with updated answer positions."""

import random
import json

# Store all questions Q69-Q131 with ans:3 that need shuffling
questions_q69_q131 = """
Q69: ["A deployment script","A test case for the system","A line of code in the system","A conditional capability needed by a user to solve a problem or achieve an objective"]
Q73: ["Interviews, scenarios, use cases, and prototypes","Planning, design, coding, and testing","Coding, testing, deployment, and maintenance","Feasibility, elicitation, specification, and validation"]
Q74: ["Release the system to production environment","Execute test cases on the software","Document and write the SRS paper","Assess if needs can be satisfied cost-effectively"]
Q75: ["Executing unit tests on source code","Deploying and releasing the software","Writing code based on developer guesses","Deriving requirements through observation and discussion"]
Q76: ["Structured","Verifiable","Concise","Black-box view"]
Q77: ["Conceptual Integrity","Structured","Concise","Verifiable"]
Q78: ["Only about security","Only about performance","Vague and flexible","Complete and Consistent (no contradictions)"]
Q79: ["Only user interface presentation aspects","Only database schema and storage","Specific system features like login modules","Quality attributes affecting the entire system"]
Q80: ["Meeting system performance benchmarks","System readiness for deployment phase","Source code quality and structure standards","Validity, consistency, completeness, realism"]
Q81: ["Automated consistency analysis","Test-case generation","Reviews","Prototyping"]
Q82: ["Making prototypes of the proposed system","Writing formal use case documents","Conducting structured interview sessions","Observing and analyzing how people actually work"]
Q83: ["A database table record","A pre-written test case","Only the system administrator","A person or system using the system being built"]
Q84: ["Performance measurements under system load","Alternative paths when errors occur","What happens if the system crashes","Ideal flow when everything succeeds"]
Q85: ["Requirement specification and documentation","Requirement classification and organization","Requirements discovery and gathering","Requirements prioritization and negotiation"]
Q86: ["Testing software thoroughly before release","Deploying software to production environment","Writing and coding the source code","Transforming requirements into suitable form"]
Q87: ["Systems processing data in batches","Systems that control embedded devices","Applications accessed via the internet","Applications running on a local computer"]
Q88: ["Systems that process data in batches","Software for entertainment purposes","Applications accessed on the web","Software systems controlling hardware devices"]
Q89: ["Database design and schema creation","Component design and implementation","Interface design and specification","Architectural design of the system"]
Q90: ["A fully deployed application system","Automated test cases for validation","Compiled source code and executables","Design document describing system architecture"]
Q91: ["Writing automated test cases and scripts","Creating database tables and schemas","Writing the user interface code only","Specifying interfaces between system components"]
Q92: ["Testing database server performance loads","Deploying database to production servers","Writing SQL queries for data access","Designing data structures and database schema"]
Q93: ["A specialized testing framework only","A platform for deploying software","A database management system only","Environment coordinating tools for development"]
Q94: ["Google Chrome web browser application","Adobe Photoshop image editing software","Microsoft Word document processor","Eclipse, Visual Studio, or NetBeans"]
Q95: ["Computer Analysis and System Evaluation","Coding and Software Engineering concepts","Complete Application Software Environment","Computer Aided Software Engineering"]
Q96: ["Specialized testing tools only","Only software design and modeling tools","Physical desks or tables for developers","Integrated tools supporting development stages"]
Q97: ["Only for open-source software projects","Workbench includes no tools by default","The workbench is free and has no cost","Users can integrate their own custom tools"]
Q98: ["Tool that analyzes code at runtime","Static analysis and checking tool","Combines object files into executable","Language compiler that creates object code"]
Q99: ["Is the software deployed correctly?","Does the product meet user expectations?","Have we built the right product?","Have we built it right per specifications?"]
Q100: ["Does the code follow structure conventions?","Have we built it right per specifications?","Does the product meet system specifications?","Have we built the RIGHT product needed?"]
Q101: ["A violation of coding style conventions","A timeout or network connection problem","A feature requested but not implemented","Any variance from attributes causing dissatisfaction"]
Q102: ["A requirement missing from documentation","A temporary network connection timeout","A user bug report or complaint","A condition causing system failure to perform"]
Q103: ["A missing or absent test case","An error in the design documentation","A fault or bug in the source code","System inability to perform per specification"]
Q104: ["Testing focused on finding and exposing defects","Testing security and penetration vulnerabilities","Testing performance under heavy system load","Testing with expected normal usage scenarios"]
Q105: ["User acceptance testing of normal scenarios","Testing using typical expected user patterns","Performance load testing of the system","Testing with deliberately obscure cases"]
Q106: ["Validating the entire system end-to-end","Testing individual module functionality","User acceptance and satisfaction testing","Testing module integration and interfaces"]
Q107: ["Regression testing","Unit testing","Beta testing always","Alpha testing — for custom systems developed for a single client"]
Q108: ["Database schema or structure is updated","A completely new project is initiated","Source code is first being written","Changes are made to check for side effects"]
Q109: ["Teach end users how to use the system","Create user and system documentation","Prove the software has no possible defects","Expose defects before production use"]
Q110: ["Mobile applications running on devices","Systems exclusively used by government","New systems built with latest technology","Older systems using outdated technology"]
Q111: ["The application data storage","Support software and utilities","System hardware and infrastructure","Cloud API endpoints and services"]
Q112: ["Deployment always requires evolution","Software systems never require any changes","Developers enjoy rewriting code from scratch","Business changes generate new requirements"]
Q113: ["Improving system performance metrics","Adapting to new operating systems","Adding new features to the system","Fixing bugs, vulnerabilities, and errors"]
Q114: ["Testing software system components","Introducing and adding new features","Fixing and repairing bugs","Adapting software to new platforms or OS"]
Q115: ["It requires rewriting all the code","It develops entirely new functionality","Complete reengineering is always faster","Reduces risk and cost compared to replacement"]
Q116: ["Converting legacy database structures","Refactoring program code structure","Translating code between programming languages","Analyzing code to document organization"]
Q117: ["Cleaning and organizing database files","Improving the overall program structure","Analyzing and documenting code","Converting code to a newer language"]
Q118: ["Because software testing is simple","Because there are too many developers","Because software development is inexpensive","Because software is intangible and unique"]
Q119: ["The overall business market conditions","User and customer satisfaction factors","Only the software code quality","The project schedule or resources"]
Q120: ["Individual team member morale","The organization's financial situation","Only the overall project timeline","The software quality or performance"]
Q121: ["Individual developer work performance","Only the project timeline and schedule","Only the system code quality","The organization developing the software"]
Q122: ["Budget, Schedule, Staff, Implementation","Deploy, Monitor, Fix, Document","Plan, Design, Code, Test","Identify, Analyze, Plan, Monitor"]
Q123: ["Preventing or eliminating all risks","Finding and identifying new risks only","Writing down the risk management plan","Checking if risk probability or effects change"]
Q124: ["Status reporting and documentation","Human resources and team management","Risk identification and monitoring","Proposal writing to win contracts"]
Q125: ["Purchasing new hardware equipment","Hiring more developers for the team","Writing as much code as possible","Quality control and quality assurance"]
Q126: ["Portability across platforms","Usability and ease of interface","System reliability and uptime","Correctness of implementation"]
Q127: ["How easily the system can be deployed","How fast the software performance is","How simple the user interface is","The effort to find and fix a fault"]
Q128: ["The software is developed open source","The software works without internet","The software size is small","The effort to transfer software to other platforms"]
Q129: ["The software deployment procedures","Only the coding and style standards","The project budget and timeline","Quality controls and activities to verify quality"]
Q130: ["The organizational team structure","The project timeline and schedule","Rules prescribing how to do something","A measurable attribute norm for compliance"]
Q131: ["How easy the system is to use","How secure the software system is","How fast the system performance is","The effort to work with other software"]
""".strip()

# Parse the data
questions = {}
for line in questions_q69_q131.split('\n'):
    if ':' in line:
        qid_str, opts_str = line.split(':', 1)
        qid = int(qid_str.replace('Q', '').strip())
        # Parse the JSON array
        opts = json.loads(opts_str.strip())
        questions[qid] = opts

print(f"Parsed {len(questions)} questions with ans:3")

# Generate shuffled versions with deterministic seeding
output_lines = []
answer_dist = {0: 0, 1: 0, 2: 0, 3: 0}

for qid in sorted(questions.keys()):
    opts = questions[qid]
    
    # Seed based on question ID for reproducibility
    random.seed(qid * 19)  # Prime number for varied distribution
    
    # Create indices array [0, 1, 2, 3]
    indices = [0, 1, 2, 3]
    random.shuffle(indices)
    
    # Shuffle options
    shuffled_opts = [opts[i] for i in indices]
    
    # Find new answer position (where original index 3 ended up)
    new_ans = indices.index(3)
    answer_dist[new_ans] += 1
    
    # Format the options for output 
    opts_str = ','.join([f'"{opt}"' for opt in shuffled_opts])
    
    output_lines.append({
        'qid': qid,
        'opts': shuffled_opts,
        'new_ans': new_ans,
        'opts_str': opts_str
    })

# Print summary
print(f"\nNew answer distribution:")
for pos in sorted(answer_dist.keys()):
    print(f"  Position {pos} (Answer {chr(65+pos)}): {answer_dist[pos]} questions")

# Write to file in the format that can be copy-pasted
with open('SHUFFLED_Q69_Q131.txt', 'w') as f:
    f.write("// SHUFFLED QUESTIONS Q69-Q131 WITH RANDOMIZED ANSWER POSITIONS\n")
    f.write("// Replace these question definitions in your QUESTIONS array\n")
    f.write("// Below is the complete corrected code for Q69-Q131\n\n")
    
    for item in output_lines:
        qid = item['qid']
        new_ans = item['new_ans']
        opts_str = item['opts_str']
        
        # We'll create a minimal version showing the key changes
        f.write(f"{{ id:{qid}, ")
        f.write(f"opts:[{opts_str}], ")
        f.write(f"ans:{new_ans} }}\n")

print("\n✓ Output written to SHUFFLED_Q69_Q131.txt")

# Also write a JavaScript-formatted version
with open('SHUFFLED_QUESTIONS.js', 'w', encoding='utf-8') as f:
    f.write("// SHUFFLED QUESTIONS Q69-Q131\n")
    f.write("// Answer positions have been randomized and redistributed\n")
    f.write("// Replace the original Q69-Q131 in your QUESTIONS array with these\n\n")
    
    for item in output_lines:
        qid = item['qid']
        new_ans = item['new_ans']
        opts_str = item['opts_str']
        f.write(f"  {{ id:{qid}, ")
        f.write(f"opts:[{opts_str}], ")
        f.write(f"ans:{new_ans} }}\n")

print("✓ JavaScript version written to SHUFFLED_QUESTIONS.js")

# Now write mapping of changed answers for verification
with open('ANSWER_CHANGES.txt', 'w') as f:
    f.write("QUESTION ID | OLD ANS | NEW ANS | CHANGE\n")
    f.write("=" * 50 + "\n")
    for item in output_lines:
        qid = item['qid']
        old_ans = 3  # All original had ans:3
        new_ans = item['new_ans']
        f.write(f"Q{qid:3d}        | {old_ans}       | {new_ans}       | {chr(65+old_ans)} → {chr(65+new_ans)}\n")

print("✓ Answer change mapping written to ANSWER_CHANGES.txt")


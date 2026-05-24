|  |  |  |
| --- | --- | --- |
|  |  |  |

|  |  |
| --- | --- |
|  |  |

|  |  |
| --- | --- |
| CS251 – Introduction to Software Engineering |  |

CS251 – Introduction to Software
Engineering
Lecture 10 & 11: Model to Code
Slides authored by unknown
Mohammad El-Ramly, PhD
Winter 2026

| Overview of This Lecture |
| --- |
|  |
| Basic Implementation Steps. ■ Class Diagram Implementation ■ Implementing Classes ❑ Class Association: ❑ Navigation direction; ■ Multiplicity constraint; ■ Qualified associations; ■ Association classes. ■ Implementing Statecharts ■ |

Overview of This Lecture
Basic Implementation Steps.
■
Class Diagram Implementation
■
Implementing Classes
❑
Class Association:
❑
Navigation direction;
■
Multiplicity constraint;
■
Qualified associations;
■
Association classes.
■
Implementing Statecharts
■
2

| Requirement |
| --- |
| Analysis |
| Design |
| Implement |
| Testing |

Where are we now?
Requirement
Analysis
Translate Design
Design ■
into Code
Implement
Testing
3
scihtE
ssecorP
erawtfoS
lortnoC
noisreV
erawtfoS

| Implementation: Overview |
| --- |
|  |

|  |
| --- |
|  |

|  |
| --- |
| 4 |

Implementation: Overview
Inputs:
■
Detailed UML Class Diagram;
❑
UML Sequence Diagram;
❑
UML State Diagram (if needed)
❑
Output:
■
Code - Implementation of the given model
❑
as described
Note: other aspects of design (not discussed here)
■
include: data structure, algorithms, database, UI,…
4

| Implementation: Overview |
| --- |
|  |

Implementation: Overview
Reminder:
■
Class diagrams give a static view of the
❑
system and the model, control and
boundary classes in it.
Sequence diagrams show the basic
❑
behavior of some of the operations.
A state diagram describes a complete
❑
lifetime for classes with complex behavior
5

CPSC-4360-01, CPSC-5360-01, Lecture 9 6

| 1. Basic Steps in Implementation |
| --- |
| 1- Define method interface: Give a formal/informal description of the ❑ functionality of an operation and parameters; Useful in reducing misunderstanding; ❑ Allows splitting the workload. ❑ 2- Decide the order of implementation: Which class/subsystem to start. ❑ 3- Implement design in suitable programming lang. |

1. Basic Steps in Implementation
1- Define method interface:
Give a formal/informal description of the
❑
functionality of an operation and parameters;
Useful in reducing misunderstanding;
❑
Allows splitting the workload.
❑
2- Decide the order of implementation:
Which class/subsystem to start.
❑
3- Implement design in suitable programming
lang.
7

| Step 1. Defining Method Interface |
| --- |
| During design: ■ Detailed information of the method header are defined: ❑ Returned Type, Parameter Type; ■ Accessibility. ■ public, private, protected ❑ However, the functionality is not formally defined: ■ What should the method do? What is the algorithm? ❑ What are acceptable values for the parameter? ❑ Etc… ❑ |

Step 1. Defining Method Interface
During design:
■
Detailed information of the method header are defined:
❑
Returned Type, Parameter Type;
■
Accessibility.
■
public, private, protected
❑
However, the functionality is not formally defined:
■
What should the method do? What is the algorithm?
❑
What are acceptable values for the parameter?
❑
Etc…
❑
8

| Operation Contract |
| --- |
|  |

Operation Contract
Writing the operation contract is one possible way to
■
define the functionality.
Define the precondition:
■
Express the constraint regarding the attributes of the class
❑
and the actual parameter.
Define the postcondition:
■
Express the effect of an operation:
❑
Instance Creation/Deletion;
■
Attribute Modification;
■
Association Formed/Broken.
■
Description can scale in formality.
■
9

| Operation Contract: Example
withdraw() |  |
| --- | --- |

| BankAccount |
| --- |
| - balance |
| + deposit (amt : float) + withdraw (amt : float) |

|  | Functionality
(Contract) |
| --- | --- |
| Precondition: - amt > 0 - amt <= balance Postcondition: - New balance = Old balance - amt |  |

Operation Contract: Example
withdraw()
BankAccount
- balance
+ deposit (amt : float)
Interface
+ withdraw (amt : float)
Functionality
(Contract)
Precondition:
- amt > 0
- amt <= balance
Postcondition:
- New balance = Old balance - amt
10

| Step 2. Order of Implementation |
| --- |
| Many classes with dependencies in the design: ■ Need an order of implementation. ❑ Two basic strategies: ■ Top-Down: ❑ Starts with high-level components. (e.g., Sys Manager class) ■ Then continue to implement the dependent components. ■ Bottom-Up: ❑ Starts with the lower level classes, i.e., classes with least ■ dependency. (Book, Dish, etc.) Then proceed to code classes that make use of the ■ implemented classes. |

Step 2. Order of Implementation
Many classes with dependencies in the design:
■
Need an order of implementation.
❑
Two basic strategies:
■
Top-Down:
❑
Starts with high-level components. (e.g., Sys Manager class)
■
Then continue to implement the dependent components.
■
Bottom-Up:
❑
Starts with the lower level classes, i.e., classes with least
■
dependency. (Book, Dish, etc.)
Then proceed to code classes that make use of the
■
implemented classes.
11

| Example: |  |
| --- | --- |
|  |  |

|  |
| --- |
|  |

|  |
| --- |
| 12 |

Example:
12

|  | Example: Top Down |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

|  |
| --- |
| 13 |

Example: Top Down
13

| Example: Top Down |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

|  |
| --- |
| 14 |

Example: Top Down
14

| Example: Top Down |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |

|  |
| --- |
| 15 |

Example: Top Down
15

| Example: Top Down |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

|  |
| --- |
|  |

|  |
| --- |
| 16 |

Example: Top Down
16

| Example: Top Down |  |
| --- | --- |
|  |  |

|  |
| --- |
|  |

|  |
| --- |
| 17 |

Example: Top Down
17

|  |
| --- |
| A myB B methodA() methodB() |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| A |  | myB |  |  |
| methodA() |  |  |  |  |

Example
A myB B
methodA() methodB()
{
myB.methodB();
}
## A B
A depends on B, i.e., A makes use of B
myB may be an attribute in class A of class B;
■
The navigability is one possible indicator of the dependency.
■
18

| Top Down Implementation |
| --- |
|  |

|  |
| --- |
|  |

|  |
| --- |
| 19 |

Top Down Implementation
Starts with Class A, then Class B.
■
Advantages:
■
Class A represents a higher level component as it makes use
❑
of other classes.
Starting with high level components enables early validation
❑
of the overall system.
Disadvantages:
■
Need temporary implementation (known as stub) for lower
❑
classes.
Example:
❑
A temporary implementation of methodB() is needed for
■
the implementation of methodA().
19

Bottom Up Implementation
Starts with Class B, then Class A.
■
Advantages:
■
Low level classes can usually stand alone.
❑
No need for stub.
❑
Disadvantages:
■
Have to postpone the generation of a complete
❑
executable program.
20

|  | Example: Bottom Up |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

|  |
| --- |
|  |

|  |
| --- |
| 21 |

Example: Bottom Up
21

| Example: Bottom Up |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |

|  |
| --- |
|  |

|  |
| --- |
| 22 |

Example: Bottom Up
22

| Example: Bottom Up |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |

|  |
| --- |
|  |

|  |
| --- |
| 23 |

Example: Bottom Up
23

| Example: Bottom Up |  |
| --- | --- |
|  |  |
|  |  |
|  |  |

|  |
| --- |
|  |

|  |
| --- |
| 24 |

Example: Bottom Up
24

| Example: Bottom Up |  |
| --- | --- |
|  |  |

|  |
| --- |
|  |

|  |
| --- |
| 25 |

Example: Bottom Up
25

2. Class Diagram
Implementation
26

2.1 Implementing Classes
Basic mapping:
■
A UML Class is implemented by a class in Java,
❑
C++, etc;
Attributes are implemented by fields;
❑
Operations are implemented by methods.
❑
There may be some language specific issues:
■
E.g., the implementation of abstract classes,
❑
interfaces, and generalization.
27

|  | #
#
+
+
+ |  |
| --- | --- | --- |
|  | # |  |
|  |  |  |
|  | # |  |
|  |  |  |
|  | + |  |
|  |  |  |
|  | + + |  |
|  |  |  |

| The getCovers(c:Integer) operation should be setCovers(c:Integer). |  |
| --- | --- |
|  | :Integer). |

| The getCovers(c:In |
| --- |
|  |

Example: The Class
Booking
public abstract class Booking {
protected int covers;
# protected Date date;
#
+
protected Booking(int c, Date d) {
+
covers = c;
+
date = d;
}
public void setCovers(int c) {
covers = c;
}
public Date getDate() { return date; }
public void setArrivalTime(Time t) { }
}
The getCovers(c:Integer) operation should be setCovers(c:Integer).
28

| Class Model to Java Mapping |
| --- |
| class Account { …} Account abstract class Account {…} Account Account {abstract} <<interface>> interface Payable {…} Payable |
| 29 |

|  | Class Model to Java Mapping |  |
| --- | --- | --- |
| clas Account |  |  |

Class Model to Java Mapping
class Account { …}
Account
abstract class Account {…}
Account
Account
{abstract}
<<interface>>
interface Payable {…}
Payable
29

| Class Model to Java Mapping
<<enum>>
OrderStatus
⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯
⎯
- CREATED : int = 0
- SHIPPED : int = 1
- DELIVERED : int = 2
public enum OrderStatus {
private int CREATE = 0;
private int SHIPPING = 1;
private int DELIVERED = 2;
} 30 |  |
| --- | --- |
|  | public enum OrderStatus { private int CREATE = 0; private int SHIPPING = 1; private int DELIVERED = 2; } 30 |

|  | Class Model to Java Mapping |
| --- | --- |
| <<enum>> OrderStatus ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ - CREATED : int = 0 - SHIPPED : int = 1 |  |

|  | } |
| --- | --- |

Class Model to Java Mapping
<<enum>>
OrderStatus
⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯
⎯
- CREATED : int = 0
- SHIPPED : int = 1
- DELIVERED : int = 2
public enum OrderStatus {
private int CREATE = 0;
private int SHIPPING = 1;
private int DELIVERED = 2;
} 30

| Class Model to Java Mapping |  |
| --- | --- |
| Account SavingsAccount class Account { …} class SavingsAccount extends Account {…} |  |
| 31 |  |

| Class Model to Java Mapping |
| --- |
|  |

Class Model to Java Mapping
Account
SavingsAccount
class Account { …}
class SavingsAccount extends Account {…}
31

| Class Model to Java Mapping
<<interface>> |
| --- |
| Payable Invoice class Payable { …} class Invoice implements Payable {…} 32 |

| <<interface>> |
| --- |
| Payable |

Class Model to Java Mapping
<<interface>>
Payable
Invoice
class Payable { …}
class Invoice implements Payable {…}
32

| Class Model to Java Mapping |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| UML Types ■ Boolean ❑ Integer ❑ Real ❑ String ❑ | ■ | JavaTypes boolean ❑ int ❑ float or double ❑ String ❑ |  |  |
| Tool may use J ■ | a |  |  | be |
| Default depend ■ int and for re |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

Class Model to Java Mapping
UML Types JavaTypes
■ ■
Boolean boolean
❑ ❑
Integer int
❑ ❑
Real float or double
❑ ❑
String String
❑ ❑
Tool may use Java types instead
■
Default depends on tool; it could be
■
int and for return value void
33

| The setArrivalTime() operation should be setArrivalTime(Time t). |  |
| --- | --- |
|  | Time t). |

| The setArrivalTime |
| --- |
|  |

Example: Generalization
public class WalkIn
extends Booking {
public WalkIn(...) { ... }
}
public class Reservation
extends Booking {
Time arrivalTime ;
public Reservation(...) { ... }
public void setArrivalTime(Time t) {
arrivalTime = t ;
}
}
The setArrivalTime() operation should be setArrivalTime(Time t).
34

CPSC-4360-01, CPSC-5360-01, Lecture 9 35

| Overview of This Lecture |
| --- |
|  |
| Basic Implementation Steps. ■ Class Diagram Implementation ■ Implementing Classes ❑ Class Association: ❑ Navigation direction; ■ Multiplicity constraint; ■ Qualified associations; ■ Association classes. ■ Implementing Statecharts ■ |

Overview of This Lecture
Basic Implementation Steps.
■
Class Diagram Implementation
■
Implementing Classes
❑
Class Association:
❑
Navigation direction;
■
Multiplicity constraint;
■
Qualified associations;
■
Association classes.
■
Implementing Statecharts
■
36

| Overview of This Lecture |
| --- |
|  |
| Basic Implementation Steps. ■ Class Diagram Implementation ■ Implementing Classes ❑ Class Association: ❑ Navigation direction; ■ Multiplicity constraint; ■ Qualified associations; ■ Association classes. ■ Implementing Statecharts ■ |

Overview of This Lecture
Basic Implementation Steps.
■
Class Diagram Implementation
■
Implementing Classes
❑
Class Association:
❑
Navigation direction;
■
Multiplicity constraint;
■
Qualified associations;
■
Association classes.
■
Implementing Statecharts
■
37

|  | 2.2 Implementing Associations |
| --- | --- |
| Associations (Class Diagram) describe properties of links ■ (Object Diagram). |  |

2.2 Implementing Associations
Associations (Class Diagram) describe properties of links
■
(Object Diagram).
Account Guarantor
:Account :Guarantor
A link gives one object access to another and enables message
■
passing.
Java: References (C++: Object Pointer) share these properties, so
■
associations can be implemented with references.
References support only one direction of navigation.
■
Should restrict navigability to make implementation easier.
❑
References should not be manipulated explicitly by other classes.
■
38

| Optional Unidirectional Association
Distinction between associations:
■ |
| --- |
| Distinction between associations: ■ |
| direction; ❑ multiplicity. ❑ Reference variables can hold: ■ a reference to another object; ❑ or the null reference. ❑ So the ‘default’ multiplicity of a reference is ‘0..1’. ■ |

Optional Unidirectional Association
Distinction between associations:
■
direction;
❑
multiplicity.
❑
Reference variables can hold:
■
a reference to another object;
❑
or the null reference.
❑
So the ‘default’ multiplicity of a reference is ‘0..1’.
■
39

| Implementation |
| --- |
|  |

Implementation
The association is defined by a field in the
■
Account Java class holding a reference to an
instance of the DebitCard Java class:
public class Account {
private DebitCard theCard ;
...
}
Good match for
simple object
0..1 reference.
Account DebitCard
40

| Maintaining the Association |
| --- |
|  |
| As only Account is “aware” of this association, it ■ should also maintain the association: Setup/Removal of the link; ❑ Appropriate methods for accessing the linked object. ❑ |

Maintaining the Association
As only Account is “aware” of this association, it
■
should also maintain the association:
Setup/Removal of the link;
❑
Appropriate methods for accessing the linked object.
❑
e.g. public DebitCard getCard(){
return theCard;
Return the
}
linked object
to outsider
public void setCard(DebitCard card){
theCard = card;
Changing the
}
linked object
41

| Mutability for Association |
| --- |
| The last example assumes that the DebitCard ■ |

Mutability for Association
The last example assumes that the DebitCard
■
association is mutable:
An Account object can be linked to a different
❑
DebitCard object during its lifetime.
Hence, it makes sense to have the following methods
■
for setup/removal the link:
public void setCard(DebitCard card){
theCard = card;
}
public void removeCard( ) {
theCard = null;
}
42

| Immutable Association |
| --- |
| Some associations are immutable: |
| ■ once assigned, a link must not be altered. ❑ The designer can state this in the class diagram: ■ |

|  |
| --- |
| { } Immutable |

| { }
Immutable |
| --- |
|  |

Immutable Association
Some associations are immutable:
■
once assigned, a link must not be altered.
❑
The designer can state this in the class diagram:
■
{ }
Immutable
The programmer has to check the link’s existence
■
explicitly:
Explicit Check to
public void setCard(DebitCard card) {
maintain Immutable
if (theCard != null) {
// throw ImmutableAssociationException link
}
If there is a card, you
theCard = card ;
cannot change it
}
43

| Compulsory Association |
| --- |
|  |

|  |
| --- |
|  |

|  |
| --- |
|  |

Compulsory Association
Multiplicity with lowerbound larger than 0 is compulsory,
■
i.e., “At all times, the link(s) cannot be null”.
Example:
■
The above means “An Account object must have exactly
■
one link to a Guarantor object at all times”.
Programmers have to check explicitly to ensure this is true.
■
44

| Implementation |
| --- |
| The earliest possible opportunity to setup the link |

|  |
| --- |
| public setGuarantor(Guarantor g) { if (g == null) { // throw NullLinkError } theGuarantor = g ; } |

Implementation
The earliest possible opportunity to setup the link
■
is in the constructor method:
public Account(Guarantor g) {
if (g == null) { Make sure we
// throw NullLinkError have a
}
guarantor
theGuarantor = g ;
}
If the association is mutable, similar checks must be
■
performed in methods that changes the link, e.g.:
public setGuarantor(Guarantor g) {
if (g == null) { Make sure we
// throw NullLinkError have a
}
guarantor
theGuarantor = g ;
}
45

CPSC-4360-01, CPSC-5360-01, Lecture 9 46

|  | 1-to-Many Unidirectional Association |  |
| --- | --- | --- |
| Some associations require more than one link to ■ be stored: | Some associations require more than one link to ■ |  |

|  |
| --- |
|  |

1-to-Many Unidirectional Association
Some associations require more than one link to
■
be stored:
Data structures, such as arrays and ArrayLists, can be used
■
to store the references.
For a specific upper bound, e.g., “0…8”, specific checks must be
❑
implemented:
public class Manager {
private ArrayList<Account> theAccounts ;
*
Stores
public void addAccount(Account acc) {
Accounts
theAccounts.add(acc) ;
references.
}
}
47

| Bidirectional Association |
| --- |
| Some associations need to be navigated in bot |

| Account |
| --- |
| theCard: DebitCard |

| DebitCard |
| --- |
| theAccount: Account |

|  |  | theCard |  |
| --- | --- | --- | --- |
|  | theAccount |  |  |
|  |  |  |  |
|  |  |  |  |

Bidirectional Association
Some associations need to be navigated in both
■
directions:
because references are unidirectional, it will take two
❑
references to implement a bidirectional link;
the association can be implemented by including a
❑
suitable field in each of the associated classes.
Bidirectional Association
Account DebitCard
stated in Class Diagram
Closest
Account theCard DebitCard implementation of
theAccount
the Class Diagram in
theCard: DebitCard theAccount: Account
Java or C++
48

| Bidirectional Association Implementation |  |
| --- | --- |

|  |
| --- |
|  |

|  |
| --- |
|  |

| {
Account acc1 = new Account() ;
DebitCard aCard = new DebitCard(acc1) ;
acc1.setCard(aCard) ;
} |  |
| --- | --- |
|  |  |

| uestion: Why is that the order of |
| --- |
|  |

Bidirectional Association Implementation
DebitCard is optional (“0..1” from Account).
■
Account is compulsory (“1” from DebitCard).
■
Hence, the best way to satisfy the conditions is:
■
Create the Account first, then the DebitCard:
❑
{
Account acc1 = new Account() ;
DebitCard aCard = new DebitCard(acc1) ;
acc1.setCard(aCard) ;
}
Question: Why is that the order of associations creation to satisfy the conditions?
49

| Referential Integrity |
| --- |
| The bidirectional association is implemented as two ■ |

| theCard |
| --- |
|  |

| acc1: Account |  | theAccount |
| --- | --- | --- |

Referential Integrity
The bidirectional association is implemented as two
■
separate references, it is important to keep them consistent.
The links should be “inversed” one to each other.
❑
Known as referential integrity.
❑
Example of referential integrity violation:
■
Account acc1 = new Account() ;
Account acc2 = new Account() ;
DebitCard aCard = new DebitCard(acc1);
acc2.setCard(aCard) ;
theCard
The two links do not
acc2: Account aCard: DebitCard
correspond to a valid
bidirectional
theAccount
acc1: Account association!
50

|  | Maintaining Referential Integrity |
| --- | --- |
| The problem with the example code on last slide: ■ DebitCard creation and reference setup (setCard() ❑ method) are two separate operations. Responsibility of programmer to make sure the two ❑ operations are performed in a consistent fashion. To minimize the human error, delegate one of the classes ■ to maintain the referential integrity instead. Example: ■ | The problem with the example code on last slide: |

Maintaining Referential Integrity
The problem with the example code on last slide:
■
DebitCard creation and reference setup (setCard()
❑
method) are two separate operations.
Responsibility of programmer to make sure the two
❑
operations are performed in a consistent fashion.
To minimize the human error, delegate one of the classes
■
to maintain the referential integrity instead.
Example:
■
public class Account {
private DebitCard theCard ;
Account class
handles both the
public void addCard() { DebitCard creation
theCard = new DebitCard(this); and reference setting.
}
// other methods as well
}
51

|  |
| --- |
|  |

Joint Creation of Objects
Suppose an association is intended to be immutable
■
and also needs to be traversed in both directions.
Constructors of both classes should take in an
■
instance of the other to satisfy the constraint
specified by the class diagram.
Java and C++ do not allow simultaneous object creation.
❑
Must create one of the objects with the default constructor,
❑
i.e., to violate the constraint for a short time.
52

|  |
| --- |
| Attempts to satisfy the compulsory link: ■ |

|  |  | a is not
initialized. |
| --- | --- | --- |
| Have to violate the constraint for a while: ■ |  |  |
|  |  |  |

Code Example
Attempts to satisfy the compulsory link:
■
g is not
Account a = new Account(g) ;
Guarantor g = new Guarantor(a) ; initialized.
Account a = new Account(new Guarantor(a)) ;
a is not
Guarantor g = a.getGuarantor( ) ;
initialized.
Have to violate the constraint for a while:
■
g is initialized by
default constructor, no
Guarantor g = new Guarantor( ) ;
Account reference.
Account a = new Account(g) ;
Setup the reference
g.setAccount(a) ;
after Account a is
properly initialized.
53

| Domain Model |
| --- |
|  |

| myG |  |
| --- | --- |
|  |  |

| Account |
| --- |
| myG: Guarantor |
| getMyG( ): Guarantor setMyG( Guarantor ) |

| myA: Account |
| --- |
| getMyA ( ): Account setMyA ( Account ) |

Implementing Bidirectional
Association
Domain Model
myG
Account Guarantor
myG: Guarantor myA myA: Account
getMyG( ): Guarantor getMyA ( ): Account Some likely
setMyG( Guarantor ) setMyA ( Account ) methods
Class Diagram
54

| Maintaining Bidirectional Association
Methods that change the reference should maintain |  |
| --- | --- |
|  | Methods that change the reference should maintain |

Maintaining Bidirectional Association
Methods that change the reference should maintain
■
referential integrity.
Take setMyG() for example:
■
Have to set the reversed link too.
❑
If Account has already a Guarantor:
❑
Either do not allow the link change.
■
OR, remove the link with previous Guarantor.
■
a :Account oldG: Guarantor
The Reverse link
has to be
removed too.
newG: Guarantor
a.setMyG(newG)
55

| Code Example
//Class Account |
| --- |
| //Class Account |
| public void setMyG(Guarantor newG) { if (newG == null) //throw NullLinkError if (myG != null && myG != newG) { //previous Guarantor exists myG.removeMyA(this); } if (myG == newG) return; myG = newG; //set the reverse link myG.setMyA(this); } |

Code Example
//Class Account
public void setMyG(Guarantor newG) {
if (newG == null)
//throw NullLinkError
if (myG != null && myG != newG) {
//previous Guarantor exists
myG.removeMyA(this);
}
//Class Guarantor
if (myG == newG) void removeMyA(Account a) {
return;
//only allows holder of
//the reverse link call
myG = newG;
//this method
//set the reverse link
if (a == myA)
myG.setMyA(this); myA = null;
} }
56

| Code Example (Cont)
//Class Guarantor |
| --- |
| //Class Guarantor |
| public void setMyA(Account newA) { if (newA == null) //throw NullLinkError if (myA != null && myA != newA) { //previous Guarantor exists myA.RemoveMyG(this); } if (myA == newA) return; myA = newA; //set the reverse link myA.setMyG(this); } |

Code Example (Cont)
//Class Guarantor
public void setMyA(Account newA) {
if (newA == null)
//throw NullLinkError
if (myA != null && myA != newA) {
//previous Guarantor exists
myA.RemoveMyG(this);
}
//Class Account
if (myA == newA) void RemoveMyG(Guarantor g) {
return;
//only allows holder of
//the reverse link call
myA = newA;
//this method
//set the reverse link
if (g == myG)
myA.setMyG(this); myG = null;
} }
57

| Observations |
| --- |
|  |
| Even with the complicated code, there are still some ■ problems: The old guarantor will be without an Account object. ❑ Mutual recursive functions: ❑ setMyA calls setMyG, which calls setMyA. ■ Very easy to get into infinite loop. ■ Should avoid compulsory bidirectional association if ■ possible. If bidirectional association must be used, ■ immutability is recommended to curb the coding complexity. |

Observations
Even with the complicated code, there are still some
■
problems:
The old guarantor will be without an Account object.
❑
Mutual recursive functions:
❑
setMyA calls setMyG, which calls setMyA.
■
Very easy to get into infinite loop.
■
Should avoid compulsory bidirectional association if
■
possible.
If bidirectional association must be used,
■
immutability is recommended to curb the coding
complexity.
58

CPSC-4360-01, CPSC-5360-01, Lecture 9 59

| Overview of This Lecture |
| --- |
|  |
| Basic Implementation Steps. ■ Class Diagram Implementation ■ Implementing Classes ❑ Class Association: ❑ Navigation direction; ■ Multiplicity constraint; ■ Qualified associations; ■ Association classes. ■ Implementing Statecharts ■ |

Overview of This Lecture
Basic Implementation Steps.
■
Class Diagram Implementation
■
Implementing Classes
❑
Class Association:
❑
Navigation direction;
■
Multiplicity constraint;
■
Qualified associations;
■
Association classes.
■
Implementing Statecharts
■
60

|  | 1-to-Many Unidirectional Association |  |
| --- | --- | --- |
| Some associations require more than one link to ■ be stored: | Some associations require more than one link to ■ |  |

|  |
| --- |
|  |

1-to-Many Unidirectional Association
Some associations require more than one link to
■
be stored:
Data structures, such as arrays and ArrayLists, can be used
■
to store the references.
public class Manager {
private ArrayList<Account> theAccounts ;
*
Stores
public void addAccount(Account acc) {
Accounts
theAccounts.add(acc) ;
references.
}
}
61

| 1-to-Many Unidirectional Association
0..8 |  |
| --- | --- |

| 0..8 |
| --- |
|  |

|  |  |  |
| --- | --- | --- |
|  | 0..8 |  |
|  |  |  |

| public class Manager { |
| --- |
| private ArrayList<Account> theAccounts ; public void addAccount(Account acc) { if (theAccounts.size() < 8) theAccounts.add(acc) ; else // Throw a suitable exception } } |

1-to-Many Unidirectional Association
0..8
For a specific upper bound, e.g., “0…8”, specific checks must
■
be implemented:
public class Manager {
private ArrayList<Account> theAccounts ;
public void addAccount(Account acc) {
Check that
if (theAccounts.size() < 8)
there is less
theAccounts.add(acc) ; than 8
else accounts
// Throw a suitable exception
}
}
62

|  |
| --- |
|  |

One-to-Many Bidirectional Association
Raise no new issues:
■
Customer holds a collection of references.
❑
Account holds one non-null reference.
❑
is a better choice as the “maintainer”
Customer
■
for the referential integrity:
It provides a method like addAccount() that
❑
creates a new account and set up the reference.
Similar to the addCard() method on slide 52.
❑
63

|  |
| --- |
|  |

| Previously discussed implementation techniques
■
can be used.
Recommendation:
■
Allows only one of the classes to modify the links.
❑
E.g., It makes sense to allow only the Customer to change
❑
links to Accounts and maintain the reversed link also.
Simplify the implementation as the coding logic can be
❑
considered from one direction only. |  |
| --- | --- |
|  |  |
|  | 64 |

Many-to-Many Association
Previously discussed implementation techniques
■
can be used.
Recommendation:
■
Allows only one of the classes to modify the links.
❑
E.g., It makes sense to allow only the Customer to change
❑
links to Accounts and maintain the reversed link also.
Simplify the implementation as the coding logic can be
❑
considered from one direction only.
64

|  |
| --- |
|  |

Many-to-Many Association
Another implementation technique is to reify the association:
■
The new class (e.g., Signatory in the example above) is in a
■
good position to maintain referential integrity.
:Account :Signatory :Customer
65

| Many-to-Many Association |
| --- |
|  |

Many-to-Many Association
How to we delete a signatory delSig from an
■
account
0 0
1 :Account :Signatory :Customer 1
2 2
Assume an ArrayList signatories
■
int index1 = signatories.indexOf(delSign);
❑
tempCustomer = delSig.getCustomer();
❑
int index2
❑
= tempCustomer.getSignatories.indexOf(delSign);
tempCustomer.getSignatories.remove(index2)
❑
delSig.setCustomer(null);
❑
delSig.setAccount(null);
❑
signatories.remove(index1);
❑

Qualified Association
The purpose of a qualifier is often to provide efficient
■
access to linked objects:
For example, to access accounts given only the account
❑
number;
Also to avoid a linear search through all accounts.
❑
67

| Implementing Qualifier |
| --- |
|  |
| The run-time structure involves some kind of index ■ to accounts: |

Implementing Qualifier
The run-time structure involves some kind of index
■
to accounts:
Using
accno as
index.
68

| Code Example |  |
| --- | --- |
|  |  |

| put (Object Key, Ob | ject Value) |
| --- | --- |

| get(Object Key | ): Object |
| --- | --- |

Code Example
Hash Table is a good choice to implement the index:
■
public class Bank{
private HashTable theAccounts;
public void addAccount (Account a) {
theAccounts.put(new Integer(a.getNumber()), a);
}
put (Object Key, Object Value)
public void removeAccount(int number) {
theAccounts.remove(new Integer(number));
}
public Account lookupAccount(int number) {
return
(Account) theAccounts.get(new Integer(number));
}
get(Object Key): Object
}
69

| Hash table - reminder |
| --- |
|  |
| It means a data structure that associates keys with ■ values. The primary operation it supports efficiently is a ■ lookup: given a key (e.g., a person's name), find the corresponding value (e.g., that person's telephone number). It works by transforming the key using a hash ■ function into a hash, a number that is used to index into an array to locate the desired location ("bucket") where the values should be. |

Hash table - reminder
It means a data structure that associates keys with
■
values.
The primary operation it supports efficiently is a
■
lookup: given a key (e.g., a person's name), find the
corresponding value (e.g., that person's telephone
number).
It works by transforming the key using a hash
■
function into a hash, a number that is used to index
into an array to locate the desired location ("bucket")
where the values should be.
70

|  |
| --- |
|  |

Hash table - reminder
Like arrays, hash tables provide constant-time O(1)
■
lookup on average, regardless of the number of items in
the table.
71

|  |
| --- |
|  |

Association Class
Common strategy:
■
Transform the association class into a simple class;
❑
replacing it by two associations.
72

|  |  | * |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Module |  |  |  |  |
|  |  |  |  |  |

|  |
| --- |
| Module |

|  |
| --- |
| Student |

| Registration |
| --- |
| Mark: Integer |

|  | Registration |
| --- | --- |
| * |  |
|  |  |
|  | Mark: Integer |

| :Registration |
| --- |
| Mark = 76 |

| :Registration |
| --- |
| Mark = 76 |

| :Registration |
| --- |
| Mark = 89 |

| :Registration |
| --- |
| Mark = 89 |

| Object
Diagram |  |
| --- | --- |

Implementing Association Class
*
Module Student Module Student
1
Registration * Registration
Mark: Integer Mark: Integer
Class
Class
Diagram
Diagram
:Module :Student
:Module :Student
:Registration
:Registration
Mark = 76
Mark = 76
:Student
:Student
:Registration
:Registration
Object Object
Mark = 89
Diagram Mark = 89 Diagram
73

| public class Module {
private Vector registrations;
public void enrol(Student st) {
registrations.addElement( new Registration(st) );
}
... Maintain the link
Pass
} to Registration
Stude |  |
| --- | --- |
|  | Pass Stude |

Code Example
public class Module {
private Vector registrations;
public void enrol(Student st) {
registrations.addElement( new Registration(st) );
}
... Maintain the link
Pass the
} to Registration
Student to
Registration.
class Registration {
private Student student;
private int mark;
Registration(Student st) {
Registration
student = st; mark = 0;
keeps track of
}
the Student
...
reference.
}
74

75

| Overview of This Lecture |
| --- |
|  |
| Basic Implementation Steps. ■ Class Diagram Implementation ■ Implementing Classes ❑ Class Association: ❑ Navigation direction; ■ Multiplicity constraint; ■ Qualified associations; ■ Association classes. ■ Implementing Statecharts ■ |

Overview of This Lecture
Basic Implementation Steps.
■
Class Diagram Implementation
■
Implementing Classes
❑
Class Association:
❑
Navigation direction;
■
Multiplicity constraint;
■
Qualified associations;
■
Association classes.
■
Implementing Statecharts
■
76

3. Implementing State
Diagrams
77

| Implementing Statecharts |
| --- |
| If a statechart for a class exists: ■ it gives an overall specification of the class ❑ behaviour. it can be used to structure the implementation of the ❑ operations in a systematic way. Example: Account class ■ States: InCredit, OverDrawn, Suspended. ❑ Operations: deposit, withdraw, suspend, ❑ . unsuspend |

Implementing Statecharts
If a statechart for a class exists:
■
it gives an overall specification of the class
❑
behaviour.
it can be used to structure the implementation of the
❑
operations in a systematic way.
Example: Account class
■
States: InCredit, OverDrawn, Suspended.
❑
Operations: deposit, withdraw, suspend,
❑
.
unsuspend
78

|  |  |  |
| --- | --- | --- |
| A Statechart for Account |  |  |
|  |  |  |
|  |  |  |

|  |  | event
condition
deposit [amt < -bal]
/bal += amt
action
tatechart |  |
| --- | --- | --- | --- |
|  | statechart | tatechart |  |
| amt is a positive number (precondition). ■ |  |  |  |

|  | deposit [amt < -bal]
/bal += amt
action |
| --- | --- |
| /bal += action | /bal += action |

A Statechart for Account
event
condition
deposit [amt < -bal]
/bal += amt
action
statechart
amt is a positive number (precondition).
■
79

| Implementation Steps |
| --- |
| Define States: 1. enumerate different states as constants. ■ Record an object’s current state : 2. initial state specifies what state the object is in ■ when it is created. implement this in the constructor. ■ For each operation, implement state-dependent 3. behaviour using a statement: switch one case for each state. ■ code state-specific actions. ■ |

Implementation Steps
Define States:
1.
enumerate different states as constants.
■
Record an object’s current state
:
2.
initial state specifies what state the object is in
■
when it is created.
implement this in the constructor.
■
For each operation, implement state-dependent
3.
behaviour using a statement:
switch
one case for each state.
■
code state-specific actions.
■
80

Implementation: Step 1 and 2
public class Account {
private final int InCredit = 0;
private final int OverDrawn = 1; Step 1:
private final int Suspended = 2; • Define States.
private int historyState;
private int state;
... ...
public Account() { Step 2:
state = InCredit; • Implements Initial
State in constructor.
}
}
- The recommendation is to use the State design pattern,
- For simplicity we use instead integer constants to identify the states.
81

|  |
| --- |
|  |

| withdraw
[amt > bal]
/bal-=amt |  |
| --- | --- |

Implementation: Step 3
public void withdraw(double amt)
withdraw
[amt <= bal] {
/ bal-=amt
switch (State) {
case InCredit:
InCredit
if (amt > bal) {
state = Overdrawn;
}
bal -= amt;
withdraw
break;
[amt > bal]
case Overdrawn:
/bal-=amt
case Suspended:
break;
Overdrawn
}
}
Statechart (partial)
82

| Composite States |
| --- |
|  |

Composite States
The “suspend” transition leading from the
■
composite state is shared by all substates.
Group all substates as a single case.
❑
public void suspend () {
switch (state) {
case InCredit:
Group all
case Overdrawn:
substates as one
state = Suspended; case.
break;
case Suspended:
break;
}
83

History State
- Current state to be stored when
- Last state to be reinstated
leaving the composite state.
when unsuspend is triggered.
public void suspend() {
public void unsuspend() {
switch (state) {
switch (state) {
case InCredit:
case Suspended:
historyState = state;
state = historyState;
state = Suspended;
break;
break;
// other cases // other cases
}
}
}
}
84

Exercise
Implement deposit method.
■
Implement the previous state chart using the
■
state pattern, which is a better
implementation than enumerating the states
as constants and using if or switch
statements to distinguish behavior.
CPSC-4360-01, CPSC-5360-01, Lecture 9 85

| Entry and Exit Actions |
| --- |
| Entry Action: ■ |

Entry and Exit Actions
Entry Action:
■
The code for an entry action should be executed
❑
whenever an object enters the state containing the
action.
Exit Action:
■
The code for an exit action should be executed
❑
whenever that state is left.
Example:
■
Suppose state S has:
❑
entry and exit actions defined for it, and
■
events eventF and eventG cause transitions to and from S,
■
respectively.
86

| eventF |
| --- |
| S entry /action exit /action eventG |

|  |  |  |
| --- | --- | --- |
|  |  |  |
| entry /action exit /action | en |  |

|  |
| --- |
|  |

|  |
| --- |
| 87 |

Entry/Exit Action: Implementation
eventF
## S
entry /action
exit /action
eventG
public void eventF() { public void eventG() {
switch (state) { switch (state) {
case S: case S:
break ; doExit() ;
case T: state = U ;
doEntry() ; break ;
state = S ; case U:
break ; break ;
} }
} }
For eventF(), the state T is the state that enters S; and for eventG(), the state S goes to state U.
■
87

Summary
Basic Implementation Steps
■
Implementing Class:
■
Class Association:
❑
Navigation direction
■
Multiplicity constraint
■
Qualified associations
■
Association classes
■
Implementing State charts
❑
88

Tools for Code Generation
Can generate code from model (Code
■
generation) and then if you change code, can
update mode from code (Reverse
engineering).
This is called Round Trip Engineering, RTE.
■
Visual Paradigm Community Edition
■
Or online https://online.visual-paradigm.com/
■
Another tool is UML Lab
■
https://www.uml-lab.com/en/uml-lab/academi
c/
CPSC-4360-01, CPSC-5360-01, Lecture 9 89

|  |
| --- |
| Model2Code + SOLID ■ Read Readings 10 and 11 ■ Lecture 12 and 15 ■ https://www.youtube.com/watch?v=xkVeAbj ■ MUvo (Design and code example) https://www.youtube.com/watch?v=VzOOL ■ LjrCQA&t=1068s (Model to code) |
|  |
|  |

For this week ...
Model2Code + SOLID
■
Read Readings 10 and 11
■
Lecture 12 and 15
■
https://www.youtube.com/watch?v=xkVeAbj
■
MUvo (Design and code example)
https://www.youtube.com/watch?v=VzOOL
■
LjrCQA&t=1068s (Model to code)

|  |
| --- |
| Read strategy pattern (R #12) ■ Read observer pattern (R #13) ■ Read and run code of lecture 15 ■ https://www.youtube.com/watch?v=xkVeAbjM Uvo (Design and code example) Watch Lecture 16 ■ https://www.youtube.com/watch?v=9RtpXNcoz Wg&list=PLamDRyk2dVb6y4jFZREDy8rMcXIh iR2CB&index=34 |
|  |
|  |

For next week ...
Read strategy pattern (R #12)
■
Read observer pattern (R #13)
■
Read and run code of lecture 15
■
https://www.youtube.com/watch?v=xkVeAbjM
Uvo (Design and code example)
Watch Lecture 16
■
https://www.youtube.com/watch?v=9RtpXNcoz
Wg&list=PLamDRyk2dVb6y4jFZREDy8rMcXIh
iR2CB&index=34

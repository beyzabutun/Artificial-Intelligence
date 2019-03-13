% CS-E4800 Artificial intelligence
% Round: Applications via Logic Programming
%
% Base Encoding for the ASP Exercise: Graph Coloring
%
%
% A number of graph instances is included for testing purposes.

% Parameters: the number of colors

#const n=3.

% Define the range of colors from 1 to n

color(1..n).

% Extract the nodes of the graph from the edge/2 relation

node(X) :- edge(X,_).
node(Y) :- edge(_,Y).

% Choose a color C for each node X. By default the color can be C as
% long as there is no exceptions, i.e., X is colored by some other color
% than C. Use some auxiliary predicate to encode the exceptions.
 
hascolor(X,C) :- node(X), color(C), not nothascolor(X,C).
nothascolor(X,C):- node(X), color(C), color(C1), hascolor(X,C1), C!=C1.
% Add rules as needed

% Check the coloring condition for every edge of the graph:
% X and Y should have different colors.

:- edge(X,Y), hascolor(X,C), hascolor(Y,C).
% Extract solution (the following predicates are used in the evaluation)

#show hascolor/2.
#show edge/2.


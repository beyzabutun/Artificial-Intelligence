% CS-E4800 Artificial intelligence
% Round: Applications via Logic Programming
%
% Base Encoding for the ASP Exercise: Tournament Scheduling
%


% Parameters: the number of teams (silently assumed to be even)

#const n=4.

% Declare the domains for the teams, fields, and weeks

team(1..n).
field(1..n/2).
week(1..(n-1)).

% Define matches (an ordered pair of teams)

match(T1,T2) :- team(T1), team(T2), T1 != T2, not match(T2,T1), T1 < T2.

% Choose the week W for the match between T1 and T2 by default,
% unless the match is organized some other week. Encode exceptions
% using an appropriate auxiliary predicate.

thisweek(T1,T2,W) :- match(T1,T2), week(W), not notThisWeek(T1,T2,W).
notThisWeek(T1,T2,W) :- match(T1,T2), week(W), week(W1), thisweek(T1,T2,W1), W!=W1.
% Add rules as needed 

% Choose the field F for the match between T1 and T2 by default,
% unless the match takes place in some other field. Encode exceptions
% using an appropriate auxiliary predicate.

thisfield(T1,T2,F) :- match(T1,T2), field(F), not notthisField(T1,T2,F).
notthisField(T1,T2,F) :- match(T1,T2), field(F), field(F1), thisfield(T1,T2,F1), F!=F1.

% Add rules as needed

% Every slot (F,W) in the schedule, identified by a field F and a week W,
% must have a match scheduled

occupied(W,F) :- week(W), field(F), team(T1), team(T2), match(T1,T2), thisweek(T1,T2,W), thisfield(T1,T2,F).
:- week(W), field(F), not occupied(W,F).

% A team may have only one match per week

opponent(T1,W,T2) :- week(W), match(T1,T2), thisweek(T1,T2,W).
opponent(T2,W,T1) :- week(W), match(T1,T2), thisweek(T1,T2,W).
:- opponent(T,W,T1), opponent(T,W,T2), T1!=T2.

% Combine the schedule into a single relation for the ease of understanding

match(T1,T2,F,W) :- team(T1), team(T2), week(W), field(F), match(T1,T2), thisweek(T1,T2,W), thisfield(T1,T2,F).

% Extract solution (the following predicates are used in the evaluation)

#show match/4.
#show team/1.


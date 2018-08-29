include "alldifferent.mzn";

int: m ;
int: n ;
array [1..n, 1..m] of int: M;

array [1..n] of var 1..n:  orderofjobs;
% array [1..n] of var 1..n:  jobsinline;
array [1..n,1..m] of var 0..10000: starttime; 
array [1..n,1..m] of var 0..10000: endtime;
var int : makespan ;

% constraint forall (i in 1..n) ( jobsinline[ orderofjobs[i] ] = i);
constraint forall( i in 1..n, j in 1..m )
                    ( endtime[orderofjobs[i],j] - starttime[orderofjobs[i],j] = M[i,j] );

% machine cannot be use in same time 
constraint forall( i1 in 1..n, i2 in 1..n, j in 1..m )
                    ( if  orderofjobs[i1] >  orderofjobs[i2] 
                      then starttime[ orderofjobs[i1] , j] >= endtime[ orderofjobs[i2],j]
                      else true
                      endif   );

% the jobs cannot be use at the same time 
constraint forall( i in 1..n, j1 in 1..m, j2 in 1..m )
                    ( if  j1 > j2 
                      then starttime[ i,j1] >= endtime[ i,j2]
                      else true
                      endif   );

constraint makespan = max(endtime);
constraint alldifferent( orderofjobs);


solve minimize makespan;


output [show( orderofjobs)++show(makespan)]
++ 
["\n start time "]
++
[   if j =1 
    then "\n" 
    else ":" 
    endif ++ show(starttime[i,j]) ++"-" ++show(endtime[i,j])++"-" ++ show(orderofjobs[i])  | i in 1..n,j in 1..m
    ]


# vip language.

The first iteration of our ‘vip’ compiler includes the scanner (tokens) and the parser with the grammar rules. We have also developed a diagram_converter that converts a flow diagram to a mid-stage code representation.

The second iteration includes the semantic cube and var and function tables generation. We also linked the generated code (from the diagram) to our syntax checking.

The third iteration includes functionality to do numerical computations, assignments, conditions and whiles.

The fourth iteration includes cicles. Also we added funcitionality for ifs, elifs and elses. Added functionality to handle quadruples in a more ordered way.

The fifth iteration is finally a semi functional version. We generate the object code with the quadruples and constants table. The virtual machine sets and gets addresses and it correctly runs simple inputs that don't have functions nor arrays.

The sixth iteration includes array funcionality. vip Arrays allow you to define dimension intervals. e.g. int A[3 .. 6]; or just define the size of the dimension if no interval is given e.g. int A[4] (which goes from 0 to 3). We also have function calls, return value doesn't work yet.

The final version of our vip language is fully functional. We create diagram flows using LucidChart and then export them as CSV files where each tab is a different program. The CSV file is then converted to an intermediate code representation which is passed to the compiler as a parameter. The compiler generates the quadruples and then passes them together with the constants table to the virtual machine which finally generates the final output of the program.
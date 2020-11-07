# vip

The first iteration of our ‘vip’ compiler includes the scanner (tokens) and the parser with the grammar rules. We have also developed a diagram_converter that converts a flow diagram to a mid-stage code representation.

The second iteration includes the semantic cube and var and function tables generation. We also linked the generated code (from the diagram) to our syntax checking.

The third iteration includes functionality to do numerical computations, assignments, conditions and whiles.

The fourth iteration includes cicles. Also we added funcitionality for ifs, elifs and elses. Added functionality to handle quadruples in a more ordered way.

[Current] The fifth iteration is finally a semi functional version. We generate the object code with the quadruples and constants table. The virtual machine sets and gets addresses and it correctly runs simple inputs that don't have functions nor arrays.
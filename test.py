from graphviz import Source

# Read the DOT file containing node definitions
with open('nodes.dot', 'r') as file:
    nodes_dot = file.read()

# Create a Source object
dot_source = Source(nodes_dot)

# Save the image to a file
dot_source.render('System Map_Design Research', format='pdf', cleanup=True)

print("Horizontal Flowchart with Clustered Nodes generated successfully!")

#http://magjac.com/graphviz-visual-editor/
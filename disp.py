from graphviz import Digraph

# Create a Digraph object
dot = Digraph(comment='YOLOv8 Traffic Monitoring Architecture', format='png')
dot.attr(bgcolor='lightgray', rankdir='TB')  # Background color and Top-to-Bottom layout

# Add nodes with colors
dot.node('A', 'Start: Load Video', shape='ellipse', style='filled', fillcolor='lightgreen', color='darkgreen')
dot.node('B', 'Initialize YOLOv8 Model', shape='box', style='filled', fillcolor='lightblue', color='darkblue')
dot.node('C', 'Read Frame from Video', shape='box', style='filled', fillcolor='lightblue', color='darkblue')
dot.node('D', 'Resize Frame', shape='box', style='filled', fillcolor='lightblue', color='darkblue')
dot.node('E', 'Run YOLOv8 Detection', shape='box', style='filled', fillcolor='lightcoral', color='darkred')
dot.node('F', 'Extract Detections', shape='box', style='filled', fillcolor='lightcoral', color='darkred')
dot.node('G', 'Filter Vehicle Classes', shape='box', style='filled', fillcolor='lightyellow', color='darkorange')
dot.node('H', 'Update Tracker', shape='box', style='filled', fillcolor='lightyellow', color='darkorange')
dot.node('I', 'Check Red Line Crossing', shape='diamond', style='filled', fillcolor='cyan', color='darkcyan')
dot.node('J', 'Check Blue Line Crossing', shape='diamond', style='filled', fillcolor='cyan', color='darkcyan')
dot.node('K', 'Count Vehicles', shape='box', style='filled', fillcolor='lightpink', color='darkviolet')
dot.node('L', 'Check Emergency Vehicle Priority', shape='diamond', style='filled', fillcolor='orange', color='darkorange')
dot.node('M', 'Update Traffic Signal Logic', shape='box', style='filled', fillcolor='yellow', color='goldenrod')
dot.node('N', 'Display Frame with Annotations', shape='box', style='filled', fillcolor='lightgray', color='black')
dot.node('O', 'End: Release Video and Close Windows', shape='ellipse', style='filled', fillcolor='lightgreen', color='darkgreen')

# Add edges (flow of the process)
dot.edge('A', 'B', color='black')
dot.edge('B', 'C', color='black')
dot.edge('C', 'D', color='black')
dot.edge('D', 'E', color='black')
dot.edge('E', 'F', color='black')
dot.edge('F', 'G', color='black')
dot.edge('G', 'H', color='black')
dot.edge('H', 'I', color='black')
dot.edge('H', 'J', color='black')
dot.edge('I', 'K', color='black')
dot.edge('J', 'K', color='black')
dot.edge('K', 'L', color='black')
dot.edge('L', 'M', color='black')
dot.edge('M', 'N', color='black')
dot.edge('N', 'O', color='black')

# Add conditional edges with labels
dot.edge('I', 'L', label='Emergency Vehicle Detected', color='red', fontcolor='red')
dot.edge('J', 'L', label='Emergency Vehicle Detected', color='red', fontcolor='red')
dot.edge('K', 'M', label='Vehicle Count > 50', color='blue', fontcolor='blue')
dot.edge('L', 'M', label='Update Signal to Green', color='green', fontcolor='green')

# Add a title
dot.attr(label='YOLOv8 Traffic Monitoring Architecture', fontsize='20', fontcolor='darkblue')

# Render the flowchart
dot.render('yolov8_traffic_architecture_colored', format='png', cleanup=True)

print("Flowchart generated as 'yolov8_traffic_architecture_colored.png'")

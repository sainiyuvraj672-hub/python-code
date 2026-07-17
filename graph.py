from graphviz import Digraph

# Create DFD Level 0 (Context Diagram) for Recipe App
dfd0 = Digraph("RecipeAppDFD0", format="png")
dfd0.attr(rankdir="LR", size="8")

# External Entity (User)
dfd0.node("User", shape="rectangle")

# System
dfd0.node("System", "Recipe App System", shape="circle")

# External Entity (Database)
dfd0.node("DB", "Recipe Database", shape="rectangle")

# Connections
dfd0.edge("User", "System", label="Select Recipe / Enter Ingredients / View Steps")
dfd0.edge("System", "User", label="Show Scaled Ingredients & Step-by-Step Guide")
dfd0.edge("System", "DB", label="Fetch / Store Recipe Data")
dfd0.edge("DB", "System", label="Return Recipes & Steps")

# Render file
output_path = "/mnt/data/recipe_app_dfd_level0"
dfd0.render(output_path, format="png", cleanup=True)

output_path + ".png"

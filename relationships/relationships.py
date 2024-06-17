# Import required libraries
import ifcopenshell
import json

# Import model
model = ifcopenshell.open('/app/sherier_place_arch.ifc')

# Initialize data dictionary
data = {}

# Extract relationships
data['relationships'] = []

rels = model.by_type("IfcRelationship")
for rel in rels:
    rel_data = {
        "type": rel.is_a(),
        "global_id": rel.GlobalId,
        "relating_element": rel.RelatingElement.GlobalId if hasattr(rel, "RelatingElement") else None,
        "related_elements": [elem.GlobalId for elem in rel.RelatedElements] if hasattr(rel, "RelatedElements") else None
    }
    data['relationships'].append(rel_data)

# Save data to JSON file
output_path = "ifc_relationships.json"
with open(output_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Data has been successfully processed and saved to {output_path}")

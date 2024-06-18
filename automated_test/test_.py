import os
import json
import ifcopenshell
import pytest

# Function to run the script
def run_ifc_relationships_script():
    import ifcopenshell
    import json

    # Import model
    #model = ifcopenshell.open('/home/ec2-user/automated_test/sherier_place_arch.ifc')
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
    output_path = "/app/ifc_relationships_test.json"
    with open(output_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    return data

print("Data Loaded and Output saved to JSON successfully")

def test_ifc_file_loading():
    # Test if the IFC file loads correctly
    model = ifcopenshell.open('/app/sherier_place_arch.ifc')
    assert model is not None

def test_relationship_extraction():
    # Test relationship extraction from the IFC file
    data = run_ifc_relationships_script()
    assert 'relationships' in data
    assert len(data['relationships']) > 0

def test_output_json():
    # Test if the output JSON file is created and has the expected structure
    run_ifc_relationships_script()
    output_path = "/app/ifc_relationships_test.json"
    assert os.path.exists(output_path)
    with open(output_path) as json_file:
        data = json.load(json_file)
        assert 'relationships' in data
        assert len(data['relationships']) > 0

if __name__ == "__main__":
    pytest.main()


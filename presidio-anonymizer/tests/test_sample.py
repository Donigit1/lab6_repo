from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # Run the refactored function with known parameters
    result = sample_run_anonymizer(
        text="My name is Bond.",
        start=11,
        end=15,
        replace_with="BIP"
    )

    # Check the anonymized text
    assert result.text == "My name is BIP."

    # There should be exactly ONE item
    assert len(result.items) == 1

    item = result.items[0]

    # Validate item structure
    assert item.start == 11
    assert item.end == 14        # Bond → BIP (3 chars)
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"

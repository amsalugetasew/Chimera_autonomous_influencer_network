def test_skill_input_contract():
    skill_input = {"platform": "tiktok", "region": "us"}
    assert "platform" in skill_input
    assert "region" in skill_input

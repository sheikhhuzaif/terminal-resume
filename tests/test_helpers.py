"""Tests for helper utilities."""

import pytest
from resume.utils.helpers import format_text, validate_input


class TestFormatText:
    """Tests for format_text function."""
    
    def test_basic_formatting(self):
        """Test basic text formatting."""
        assert format_text("  hello  ") == "hello"
    
    def test_uppercase_formatting(self):
        """Test uppercase conversion."""
        assert format_text("hello", uppercase=True) == "HELLO"
    
    def test_empty_string(self):
        """Test with empty string."""
        assert format_text("") == ""


class TestValidateInput:
    """Tests for validate_input function."""
    
    def test_valid_input(self):
        """Test with valid input."""
        assert validate_input("test", min_length=1) is True
    
    def test_too_short(self):
        """Test with input too short."""
        assert validate_input("", min_length=1) is False
    
    def test_too_long(self):
        """Test with input too long."""
        assert validate_input("toolong", min_length=1, max_length=5) is False
    
    def test_exact_length(self):
        """Test with exact length match."""
        assert validate_input("exact", min_length=5, max_length=5) is True
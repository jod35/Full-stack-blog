
import pytest
from app import create_app
from ..config import TestConfig
from ..models import User,Post,Comment
from ..utils import db

# app=create_app(TestConfig)

def test_app_works():
    
    assert app.debug == True





    
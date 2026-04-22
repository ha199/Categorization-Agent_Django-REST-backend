from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from llm_helper import call_llm
import json


@api_view(['POST'])
def categorize_transaction(request):
    """
    Simple API endpoint to categorize a transaction.
    
    Request:
    {
        "description": "AWS invoice for cloud services"
    }
    
    Response:
    {
        "success": true,
        "category": "Cloud Infrastructure",
        "confidence": 0.95
    }
    """
    
    # Get description from request
    description = request.data.get('description', '').strip()
    
    # Validate input
    if not description:
        return Response(
            {
                'success': False,
                'error': 'Description is required'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if len(description) < 3:
        return Response(
            {
                'success': False,
                'error': 'Description must be at least 3 characters'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Call LLM to categorize
        result = call_llm(description)
        
        # Return response
        return Response(
            {
                'success': True,
                'description': description,
                'category': result.get('category', 'Unknown'),
                'confidence': result.get('confidence', 0.0)
            },
            status=status.HTTP_200_OK
        )
    
    except Exception as e:
        return Response(
            {
                'success': False,
                'error': f'Categorization failed: {str(e)}'
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

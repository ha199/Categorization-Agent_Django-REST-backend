from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.llm import call_llm


@api_view(["POST"])
def categorize_transaction(request):
    data = request.data

    description = data.get("description", "")

    if not description:
        return Response({"error": "description required"}, status=400)

    result = call_llm(description)

    return Response({
        "predicted_category": result["category"],
        "confidence_score": result["confidence"],
        "explanation": result.get("reason", "")
    })
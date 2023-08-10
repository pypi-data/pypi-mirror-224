from leetquery.problem import get_discription

def test_get_discription():
    problem_disc = get_discription("two-sum")
    assert isinstance(problem_disc, str) and len(problem_disc)>0
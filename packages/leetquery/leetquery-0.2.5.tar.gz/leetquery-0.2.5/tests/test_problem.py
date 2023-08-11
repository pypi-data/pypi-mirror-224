from leetquery.problem import get_discription, get_stats

def test_get_discription():
    problem_disc = get_discription("two-sum")
    assert isinstance(problem_disc, str) and \
        len(problem_disc)>0

def test_get_stats():
    stat = get_stats("two-sum")
    assert isinstance(stat, dict) and \
        list(stat.keys()) == ['totalAccepted', 'totalSubmission', 'totalAcceptedRaw', 'totalSubmissionRaw', 'acRate']

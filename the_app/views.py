from django.http import HttpResponse

from the_app.tasks import add, mul


def run_task(request):
    sum_task_id = add.delay(2, 5)
    ml_task_id = mul.delay(2, 5)
    return HttpResponse('The jobs are %s and %s' % (sum_task_id, ml_task_id))

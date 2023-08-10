import pydash
import deal
from typeguard import typechecked


@typechecked
@deal.pre(lambda _:len(_.a) > 2)
def dostuff(a):
  return pydash.flatten(a)


@typechecked
@deal.pre(lambda _:len(_.a) > 2)
def dostuff2(a):
  return pydash.flatten(a)


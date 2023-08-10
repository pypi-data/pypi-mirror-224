import pydash
import deal



@deal.pre(lambda _:len(_.a) > 2)
def dostuff(a):
  return pydash.flatten(a)

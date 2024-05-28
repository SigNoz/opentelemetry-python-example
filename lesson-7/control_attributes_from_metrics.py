import random
import time
from typing import Iterable

from opentelemetry.metrics import (
    CallbackOptions,
    Observation,
    get_meter_provider,
    set_meter_provider,
)
from opentelemetry.sdk.metrics import MeterProvider, Counter
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)
from opentelemetry.sdk.metrics.view import View

# Create a view matching the Counter instrument `requests`
# and configure the attributes in the result metric stream
# to contain only the attributes with keys with `k_3` and `k_5`
view_with_attributes_limit = View(
    instrument_type=Counter,
    instrument_name="requests",
    attribute_keys={"k_3", "k_5"},
)

exporter = ConsoleMetricExporter()

reader = PeriodicExportingMetricReader(exporter, export_interval_millis=1_000)
provider = MeterProvider(
    metric_readers=[
        reader,
    ],
    views=[
        view_with_attributes_limit,
    ],
)
set_meter_provider(provider)

meter = get_meter_provider().get_meter("reduce-cardinality-with-view", "0.1.2")

request_counter = meter.create_counter(
    name="requests",
    description="number of requests",
    unit="1",
)

while 1:
    for i in range(random.randint(1, 100)):
        request_counter.add(1, {"k_{}".format(i): "v_{}".format(i)})
    time.sleep(1)
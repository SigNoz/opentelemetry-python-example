def initialize_opentelemetry():

    # tracing setup
    from opentelemetry.trace import set_tracer_provider, get_tracer_provider
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

    set_tracer_provider(TracerProvider())
    span_processor = BatchSpanProcessor(OTLPSpanExporter())
    get_tracer_provider().add_span_processor(span_processor)

    # metrics setup
    from opentelemetry.metrics import set_meter_provider, get_meter_provider
    from opentelemetry.sdk.metrics import MeterProvider
    from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
    from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

    reader = PeriodicExportingMetricReader(
        OTLPMetricExporter(),
    )
    set_meter_provider(MeterProvider(
        metric_readers=[reader],
    ))

    # instrumentations
    from opentelemetry.instrumentation.flask import FlaskInstrumentor
    from opentelemetry.instrumentation.pymongo import PymongoInstrumentor
    from opentelemetry.instrumentation.requests import RequestsInstrumentor

    FlaskInstrumentor().instrument()
    PymongoInstrumentor().instrument()
    RequestsInstrumentor().instrument()
    # end of tracing setup
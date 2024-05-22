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
    from opentelemetry.metrics import set_meter_provider
    from opentelemetry.sdk.metrics import MeterProvider
    from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
    from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

    reader = PeriodicExportingMetricReader(
        OTLPMetricExporter(),
    )
    set_meter_provider(MeterProvider(
        metric_readers=[reader],
    ))

    import logging
    from opentelemetry._logs import set_logger_provider
    from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
        OTLPLogExporter,
    )
    from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
    from opentelemetry.sdk._logs.export import BatchLogRecordProcessor

    logger_provider = LoggerProvider()
    set_logger_provider(logger_provider)

    exporter = OTLPLogExporter()
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
    handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)

    # Attach OTLP handler to root logger
    logging.getLogger().addHandler(handler)

    # instrumentations
    from opentelemetry.instrumentation.flask import FlaskInstrumentor
    from opentelemetry.instrumentation.pymongo import PymongoInstrumentor
    from opentelemetry.instrumentation.requests import RequestsInstrumentor

    FlaskInstrumentor().instrument()
    PymongoInstrumentor().instrument()
    RequestsInstrumentor().instrument()
    # end of tracing setup
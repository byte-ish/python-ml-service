from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

def setup_telemetry(app):
    """
    Configure OpenTelemetry tracing and instrumentation.
    """
    resource = Resource.create({"service.name": "python-ml-microservice"})

    trace.set_tracer_provider(TracerProvider(resource=resource))
    tracer_provider = trace.get_tracer_provider()

    otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
    span_processor = BatchSpanProcessor(otlp_exporter)
    tracer_provider.add_span_processor(span_processor)

    FastAPIInstrumentor.instrument_app(app)
    LoggingInstrumentor().instrument()
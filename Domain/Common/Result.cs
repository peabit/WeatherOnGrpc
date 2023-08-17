namespace WeatherOnGrpc.Domain.Common;

public record Result<TValue>
{
    public bool Success { get; private init; }

    public string? Message { get; private init; }
    
    public TValue? Value { get; private init; }

    public static Result<TValue> Failed(string message)
        => new() { Message = message };

    public static Result<TValue> Ok(TValue value)
        => new() { Success = true, Value = value };
}
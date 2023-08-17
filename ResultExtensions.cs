using WeatherOnGrpc.Domain.Common;

namespace WeatherOnGrpc;

public static class ResultExtensions
{
    public static IResult ToHttpResult<TValue>(this Result<TValue> result) 
        => result.Success
            ? Results.Ok(result.Value)
            : Results.Problem(statusCode: StatusCodes.Status400BadRequest, detail: result.Message);
}
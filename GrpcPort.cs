using Grpc.Core;
using WeatherOnGrpc.Domain.CurrentWeatherInCityService;

namespace WeatherOnGrpc;

public class GrpcPort : CurrentWeatherInCityService.CurrentWeatherInCityServiceBase
{
    private readonly ICurrentWeatherService _currentWeatherService;

    public GrpcPort(ICurrentWeatherService currentWeatherService)
        => _currentWeatherService =
            currentWeatherService ?? throw new ArgumentNullException(nameof(currentWeatherService));

    public override async Task<CurrentWeatherInCityResponse> Get(
        GetCurrentWeatherInCityRequest request,
        ServerCallContext context
    )
    {
        var weatherResult = await _currentWeatherService.GetAsync(request.City);

        if (!weatherResult.Success)
        {
            return new CurrentWeatherInCityResponse();
        }

        var weather = weatherResult.Value!;

        return new CurrentWeatherInCityResponse()
        {
            City = weather.City,
            Temperature = weather.Temperature,
            Description = weather.Description
        };
    }
}
using WeatherOnGrpc.Domain.Common;

namespace WeatherOnGrpc.Domain.CurrentWeatherInCityService;

public interface ICurrentWeatherService
{
    Task<Result<CurrentWeatherInCity>> GetAsync(string city);
}
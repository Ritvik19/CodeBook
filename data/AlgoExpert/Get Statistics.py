def get_statistics(input_list):
    input_list.sort()
    n = len(input_list)
    mean = sum(input_list) / n

    middle_idx = (n - 1) // 2
    median = ((input_list[middle_idx] + input_list[middle_idx + 1]) / 2) if n % 2 == 0 else input_list[middle_idx]
    
    counts = {x: input_list.count(x) for x in set(input_list)}
    mode = max(counts.keys(), key=lambda x: counts[x])

    sample_variance = sum([(x - mean) ** 2 / (n-1) for x in input_list])

    sample_standard_deviation = sample_variance**0.5

    mean_standard_error = sample_standard_deviation / n **0.5
    z_score_standard_error = 1.96 * mean_standard_error
    mean_confidence_interval = [mean - z_score_standard_error, mean + z_score_standard_error]
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }

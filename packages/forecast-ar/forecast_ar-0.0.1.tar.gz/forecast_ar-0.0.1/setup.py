# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forecast_ar', 'forecast_ar.utils']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.7.2,<4.0.0',
 'nbsphinx>=0.9.2,<0.10.0',
 'pandoc>=2.3,<3.0',
 'prophet>=1.1.4,<2.0.0',
 'seaborn>=0.12.2,<0.13.0',
 'sktime>=0.21.0,<0.22.0',
 'sphinx-mdinclude>=0.5.3,<0.6.0',
 'sphinx>=7.1.2,<8.0.0',
 'statsforecast>=1.5.0,<2.0.0',
 'statsmodels>=0.14.0,<0.15.0',
 'tbats>=1.1.3,<2.0.0',
 'tqdm>=4.66.0,<5.0.0']

setup_kwargs = {
    'name': 'forecast-ar',
    'version': '0.0.1',
    'description': 'Automation of forecast models testing, combining and predicting',
    'long_description': '# forecast\n\n[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)\n\n## Overview\n\nforecast is a Python library built upon the foundation of the sktime library, designed to simplify and streamline the process of forecasting and prediction model aggregation. It provides tools for aggregating predictions from multiple models, evaluating their performance, and visualizing the results. Whether you\'re working on time series forecasting, data analysis, or any other predictive modeling task, forecast offers a convenient and efficient way to handle aggregation and comparison.\n\n## Key Features\n\n- **Model Aggregation:** Easily aggregate predictions from multiple models using various aggregation modes such as best model overall, best model per horizon, inverse score weighted average model, and more.\n- **Out-of-Sample Evaluation:** Evaluate model performance using out-of-sample data and choose the best models based on user-defined performance metrics.\n- **Visualization:** Visualize model performance, aggregated predictions, and prediction intervals with built-in plotting functions.\n- **Flexibility:** Accommodate various aggregation strategies, forecast horizons, and performance metrics to cater to your specific use case.\n\n## Installation\n\nInstall Your Package Name using pip:\n\n```bash\npip install forecast\n```\n\n## Usage\n\n```python\n# Import the necessary classes from your-package-name\ndata = pd.Series(np.cumsum(np.random.normal(0, 1, size=1000)), \n                 index=pd.date_range(end=\'31/12/2022\', periods=1000)).rename(\'y\').to_frame()\n\nfrom forecast.model_select import ForecastModelSelect\nForecastingModels = {\n"Naive": NaiveForecaster(),\n"AutoARIMA": StatsForecastAutoARIMA(),\n"AutoETS": StatsForecastAutoETS(),\n"AutoTheta": StatsForecastAutoTheta(),\n"TBATS": TBATS(),\n"Prophet": Prophet(),\n}\nmodel = ForecastModelSelect(\n            data= data,\n            depvar_str = \'y\',                 \n            exog_l=None,\n            fh = 10,\n            pct_initial_window=0.75,\n            step_length = 25,\n            models_d = ForecastingModels,\n            freq = \'B\',\n            mode = \'nbest_average_horizon\',\n            score = \'RMSE\', \n            nbest = 2)\n\n# compare models\nmodel.select_best(score = \'MAPE\')\n# Visualize model comparison\nmodel.plot_model_compare(score=\'MAPE\', view=\'horizon\')\nmodel.plot_model_compare(score=\'MAPE\', view=\'cutoff\')\n\n# Generate prediction\ny_pred, y_pred_ints, preds, pred_ints =  model.predict(score=\'RMSE\', ret_underlying=True)\n\n# Visualize prediction\nLFMS.plot_prediction(y_pred = y_pred,\n                     models_preds = preds,\n                     y_pred_interval = y_pred_ints, \n                     title = \'Prediction\')\n```\n\n## Documentation\n\nFor detailed information about available classes, methods, and parameters, please refer to the [Documentation](https://amineraboun.github.io/forecast/).\n\n## License\n\nThis project is licensed under the [MIT License](LICENSE).\n\n## Contributing\n\nWe welcome contributions from the community! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request. \n\n## Contact\n\nFor queries, support, or general inquiries, please feel free to reach me at [amineraboun@gmail.com](mailto:amineraboun@gmail.com).\n',
    'author': 'amineraboun',
    'author_email': 'amineraboun@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/amineraboun/forecast',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)

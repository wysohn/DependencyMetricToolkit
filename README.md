# DependencyMetricToolkit

Piece of codes that can be used to simplify calculating Dependency Management Metrics, which is covered in the book, Clean Architecture.

Only works for Java projects.

Just couldn't find the better alternative, so please let me know if there is any better one!

## Codes
The codes are not thoroughly tested, but it should be good enough for the purpose, with or without modification.

### abstractness_stats.py
Calculate the number of classes, abstract classes, and interfaces.

Then, the abstractness is calculated, as explained in Clean Architecture, as follows:

`(# of abstract classes + # of interfaces) / (# of abstract classes + # of interfaces + # of classes)`

Usage: `abstractness_stats.py ./TheFolderThatHasJavaCodes`

### stability_stats.py
Check for every source code that imports the classes/interfaces that are part of the package specified by you.

It simply checks if the prefixes that you provide (for example, java.util) are imported at least once in each source code file.

Usage: `stability_stats.py ./TheFolderThatHasJavaCodes java.util`

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code within the terms of the license.

## Acknowledgments

The DependencyMetricToolkit is powered by [OpenAI's GPT-3](https://openai.com/) language model, providing assistance in generating the content of this README.

The toolkit draws inspiration from the principles and concepts presented in the book "Clean Architecture." It aims to provide developers with simplified tools for analyzing and improving software designs.

We would greatly appreciate your feedback and suggestions on the toolkit's usefulness and any potential improvements you may have.

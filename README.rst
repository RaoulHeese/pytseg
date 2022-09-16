*****************************************
Time series segmentation toolbox (pytseq)
*****************************************

.. image:: https://github.com/RaoulHeese/pytseq/actions/workflows/tests.yml/badge.svg 
    :target: https://github.com/RaoulHeese/pytseq/actions/workflows/tests.yml
    :alt: GitHub Actions
	
.. image:: https://readthedocs.org/projects/pytseq/badge/?version=latest
    :target: https://pytseq.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status	
	
.. image:: https://img.shields.io/badge/license-MIT-lightgrey
    :target: https://github.com/RaoulHeese/pytseq/blob/main/LICENSE
    :alt: MIT License	
	
Tiny toolbox for time series segmentation.

**Usage**

Demo notebooks can be found in the "examples/" directory of this repository.

📖 **Citation**

If you find this code useful in your research, please consider citing:

.. code-block:: tex

  @misc{pytseq2022,
        author = {Raoul Heese},
        title = {pytseq},
        year = {2022},
        publisher = {GitHub},
        journal = {{GitHub} repository},
        howpublished = {\url{https://github.com/RaoulHeese/pytseq}},
       }

The implemented univariate time series segmentation closely follows:

.. code-block:: tex

  @article{PhysRevE.69.021108,
           title = {Heuristic segmentation of a nonstationary time series},
           author = {Fukuda, Kensuke and Eugene Stanley, H. and Nunes Amaral, Lu\'{\i}s A.},
           journal = {Phys. Rev. E},
           volume = {69},
           issue = {2},
           pages = {021108},
           numpages = {12},
           year = {2004},
           month = {2},
           publisher = {American Physical Society},
           doi = {10.1103/PhysRevE.69.021108},
           url = {https://link.aps.org/doi/10.1103/PhysRevE.69.021108}
          }
%global tl_name makecmds
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The new \makecommand command always (re)defines a command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makecmds
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a \makecommand command, which is like
\(re)newcommand except it always (re)defines a command. There is also
\makeenvironment and \provideenvironment for environments.


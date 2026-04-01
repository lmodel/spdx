package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Describes a certain part of a file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Snippet extends SoftwareArtifact {

  private PositiveIntegerRange lineRange;
  private File snippetFromFile;
  private PositiveIntegerRange byteRange;

}